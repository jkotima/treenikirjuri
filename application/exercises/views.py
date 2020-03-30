from application import app, db
from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user
from application.exercises.models import Exercises
from application.exercises.forms import ExerciseForm, ExerciseEditForm

@app.route("/exercises", methods=["GET"])
#@login_required
def exercises_index():
    return render_template("exercises/list.html", exercises = Exercises.query.all())

@app.route("/exercises/new/")
#@login_required
def exercises_form():
    return render_template("exercises/new.html", form = ExerciseForm())

@app.route("/exercises/delete/<exercise_id>/", methods=["POST"])
#@login_required
def exercises_delete(exercise_id):   
    e = Exercise.query.get(exercise_id)

    db.session.delete(e)
    db.session.commit()

    return redirect(url_for("exercises_index"))

@app.route("/exercises/edit/<exercise_id>/", methods=["GET"])
#@login_required
def exercises_edit(exercise_id):   
    e = Exercise.query.get(exercise_id)

    #db.session.delete(e)
    #db.session.commit()

    return render_template("exercises/edit.html", form = ExerciseEditForm(), exercise = Exercises.query.get(exercise_id))

@app.route("/exercises/edit/<exercise_id>/", methods=["POST"])
#@login_required
def exercises_update(exercise_id):
    form = ExerciseForm(request.form)   
    e = Exercise.query.get(exercise_id)

    e.name = form.name.data
    e.description = form.description.data
    e.unit = form.unit.data
    e.created_by = current_user.id

    db.session().add(e)
    db.session().commit()

    return redirect(url_for("exercises_index"))


@app.route("/exercises/", methods=["POST"])
#@login_required
def exercises_create():
    form = ExerciseForm(request.form)

    if not form.validate():
        return render_template("exercises/new.html", form = form)

    e = Exercises(form.name.data)
    e.description = form.description.data
    e.unit = form.unit.data
    e.created_by = current_user.id

    db.session().add(e)
    db.session().commit()

    return redirect(url_for("exercises_index"))

