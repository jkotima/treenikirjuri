from application import app, db
from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user

from application.events.models import Events
from application.exercises.models import Exercises
from application.sets.models import Sets

from application.events.forms import AddSetToEventForm


@app.route("/events/new", methods=["GET"])
@login_required
def events_create():
    event = Events(current_user.id)
    db.session().add(event)
    db.session().commit()

    return redirect(url_for("events_edit", event_id=event.id))

@app.route("/events/<event_id>/", methods=["GET"])
#@login_required
def events_edit(event_id):
    sets = Sets.find_sets_by_event_id(event_id)
    event = Events.query.get(event_id)

    form = AddSetToEventForm()
    form.exercise.choices = [(g.id, g.name) for g in Exercises.query.all()]

    return render_template("events/edit.html", form = form, event_id=event_id, sets=sets, event=event)


@app.route("/events/addSet/<event_id>/", methods=["POST"])
#@login_required
def events_add_set(event_id):
    form = AddSetToEventForm(request.form)
    print(form.amount.data)

    set = Sets(form.reps.data, form.amount.data, form.exercise.data, event_id)
    db.session().add(set)
    db.session().commit()

    return redirect(url_for("events_edit", event_id=event_id))