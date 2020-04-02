from application import app, db
from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user

from application.events.models import Events
from application.exercises.models import Exercises
from application.sets.models import Sets

from application.events.forms import AddSetToEventForm, CommentEventForm

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
#@login_required
def events_edit(event_id):
    sets = Sets.find_sets_by_event_id(event_id)
    event = Events.query.get(event_id)

    form = AddSetToEventForm()
    form.exercise.choices = [(g.id, g.name) for g in Exercises.query.all()]
    form2 = CommentEventForm()
    form2.comments.data = event.comment
    return render_template("events/edit.html", form = form, form2 = form2, 
                event_id=event_id, sets=sets, event=event)


@app.route("/events/addSet/<event_id>/", methods=["POST"])
#@login_required
def events_add_set(event_id):
    form = AddSetToEventForm(request.form)
    print(form.amount.data)

    set = Sets(form.reps.data, form.amount.data, form.exercise.data, event_id)
    db.session().add(set)
    db.session().commit()

    return redirect(url_for("events_edit", event_id=event_id))

@app.route("/events/delete/<event_id>/", methods=["POST"])
#@login_required
def events_delete(event_id):
    e = Events.query.get(event_id)

    #delete all sets of this event
    for s in Sets.query.filter_by(event_id = event_id):
        db.session.delete(s)

    db.session.delete(e)
    db.session.commit()

    return redirect(url_for("events_list")) 

@app.route("/events/comment/<event_id>/", methods=["POST"])
#@login_required
def events_comment(event_id):
    form = CommentEventForm(request.form)
    e = Events.query.get(event_id)
    e.comment = form.comments.data
    db.session.add(e)
    db.session.commit()

    return redirect(url_for("events_edit", event_id=event_id))       