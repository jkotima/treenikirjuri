from application import app, db
from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user

from application.programs.models import Programs
from application.workouts.models import Workouts
from application.exercises.models import Exercises

from application.programs.forms import ProgramForm, ProgramFilterForm, ProgramAddWorkoutForm, AddExerciseToWorkoutForm

@app.route("/programs/", methods=["GET"])
@login_required
def programs_index():
    created_by = request.args.get('createdBy')

    if (created_by == None):
        p = Programs.find_programs_by_creators_name("")
    else:
        p = Programs.find_programs_by_creators_name(created_by)
    
    return render_template("programs/list.html",
     programs = p, form = ProgramFilterForm(),
      active_program_name = current_user.get_active_program_name())

@app.route("/programs/new/")
@login_required
def programs_form():
    return render_template("programs/new.html", form = ProgramForm())

@app.route("/programs/", methods=["POST"])
@login_required
def programs_create():
    form = ProgramForm(request.form)

    if not form.validate():
        return render_template("programs/new.html", form = form)

    p = Programs(current_user.id, form.name.data, form.description.data)

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("programs_edit", program_id = p.id))

@app.route("/programs/edit/<program_id>/", methods=["GET"])
@login_required
def programs_edit(program_id):   
    p = Programs.query.get(program_id)
    
    #authorization
    if p.created_by != current_user.id:
        return redirect(url_for("programs_index"))

    exerciseform = AddExerciseToWorkoutForm()
    exerciseform.exercise.choices = [(g.id, g.name) for g in Exercises.query.all()]

    return render_template("programs/edit.html", program = p, workoutform = ProgramAddWorkoutForm(),
     workouts =  Workouts.query.filter_by(program_id=program_id).order_by('date_created'),
     exerciseform = exerciseform)

@app.route("/programs/<program_id>/", methods=["GET"])
@login_required
def programs_view(program_id):   
    p = Programs.query.get(program_id)

    exerciseform = AddExerciseToWorkoutForm()
    exerciseform.exercise.choices = [(g.id, g.name) for g in Exercises.query.all()]

    return render_template("programs/view.html", program = p, 
        workouts = Workouts.query.filter_by(program_id=program_id).order_by('date_created'))

@app.route("/programs/addWorkout/<program_id>/", methods=["POST"])
@login_required
def programs_add_workout(program_id):
    form = ProgramAddWorkoutForm(request.form)
    p = Programs.query.get(program_id)
    
    #authorization
    if p.created_by != current_user.id:
        return redirect(url_for("programs_index"))

    workout = Workouts(form.name.data, form.description.data, program_id)
    db.session().add(workout)
    db.session().commit()

    return redirect(url_for("programs_edit", program_id=program_id))

@app.route("/programs/activate/<program_id>/", methods=["POST"])
@login_required
def programs_activate(program_id):   
    current_user.active_program = program_id
    db.session().commit()

    return redirect(url_for("programs_index"))

@app.route("/programs/deactivate/", methods=["POST"])
@login_required
def programs_deactivate():   
    current_user.active_program = None
    db.session().commit()

    return redirect(url_for("programs_index"))

@app.route("/programs/delete/<program_id>/", methods=["POST"])
@login_required
def programs_delete(program_id):   
    p = Programs.query.get(program_id)
    
    #authorization
    if p.created_by != current_user.id:
        return redirect(url_for("programs_index"))
    
    #null Users.active_programs pointing to this program
    p.set_references_null()
    
    #delete all workouts of this program
    Workouts.query.filter(Workouts.program_id == program_id).\
        delete(synchronize_session=False)

    db.session.delete(p)
    db.session.commit()

    return redirect(url_for("programs_index"))
