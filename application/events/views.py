from application import app, db, login_manager
from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user

from application.events.models import Events
from application.exercises.models import Exercises
from application.sets.models import Sets
from application.workouts.models import Workouts


from application.events.forms import AddSetToEventForm, AddCustomSetToEventForm, CommentEventForm, SelectWorkoutForm

@app.route("/events/", methods=["GET"])
@login_required
def events_list():
    return render_template("events/list.html",
         events =  Events.query.filter_by(user_id=current_user.id).order_by('date_created'))

@app.route("/events/new", methods=["GET"])
@login_required
def events_create():
    event = Events(current_user.id)
    db.session().add(event)
    db.session().commit()

    return redirect(url_for("events_edit", event_id=event.id))

@app.route("/events/<event_id>/", methods=["GET"])
@login_required
def events_edit(event_id):
    done_sets = Sets.find_sets_by_event_id(event_id)
    event = Events.query.get(event_id)
    
    workout_arg = request.args.get('workout')
    if workout_arg:
        workout_id = int(workout_arg)
    else:
        workout_id = 0

    #authorization
    if event.user_id != current_user.id:
        return redirect(url_for("events_list"))
    
    #form inits
    form = AddCustomSetToEventForm()
    form.exercise.choices = [(g.id, g.name) for g in Exercises.query.all()]

    form2 = CommentEventForm()
    form2.comments.data = event.comment

    select_workout_form = SelectWorkoutForm()
    select_workout_form.workout.choices = [(g.id, g.name) for g in Workouts.query.filter_by(program_id=current_user.active_program)]
    
    # jos treeni valittuna -> näytille liikkeet, jotka ovat valitussa treenissä
    if workout_id != 0:
        workout = Workouts.query.get(workout_id)
        exercises = workout.get_exercises()
    else:
        exercises = []
        workout = None

    return render_template("events/edit.html", form = form, form2 = form2, select_workout_form = select_workout_form,
                            event_id=event_id, done_sets=done_sets, Sets = Sets, event=event, workout=workout, workout_id=workout_id, exercises = exercises, add_set_to_event_form = AddSetToEventForm())

@app.route("/events/addSet/<event_id>/<workout_id>/<exercise_id>/<reps>/", methods=["POST"])
@login_required
def events_add_set(event_id, workout_id, exercise_id, reps):
    form = AddSetToEventForm(request.form)
    amount = form.amount.data

    #authorization
    if Events.query.get(event_id).user_id != current_user.id:
        return login_manager.unauthorized()

    set = Sets(reps, amount, exercise_id, event_id)
    db.session().add(set)
    db.session().commit()

    return redirect(url_for("events_edit", event_id=event_id, workout=workout_id))

@app.route("/events/addSet/<event_id>/", methods=["POST"])
@login_required
def events_add_custom_set(event_id):
    form = AddCustomSetToEventForm(request.form)

    #authorization
    if Events.query.get(event_id).user_id != current_user.id:
        return login_manager.unauthorized()

    set = Sets(form.reps.data, form.amount.data, form.exercise.data, event_id)
    db.session().add(set)
    db.session().commit()

    return redirect(url_for("events_edit", event_id=event_id))

@app.route("/events/delete/<event_id>/", methods=["POST"])
@login_required
def events_delete(event_id):
    e = Events.query.get(event_id)
    
    #authorization
    if e.user_id != current_user.id:
        return login_manager.unauthorized()

    #delete all sets of this event
    for s in Sets.query.filter_by(event_id = event_id):
        db.session.delete(s)

    db.session.delete(e)
    db.session.commit()

    return redirect(url_for("events_list")) 

@app.route("/events/comment/<event_id>/", methods=["POST"])
@login_required
def events_comment(event_id):
    e = Events.query.get(event_id)
    
    #authorization
    if e.user_id != current_user.id:
        return login_manager.unauthorized()

    form = CommentEventForm(request.form)
    e.comment = form.comments.data
    db.session.add(e)
    db.session.commit()

    return redirect(url_for("events_edit", event_id=event_id))       