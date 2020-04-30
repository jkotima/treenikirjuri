from application import app, db
from flask import url_for, redirect
from flask_login import login_required
from application.sets.models import Sets


@app.route("/sets/delete/<event_id>/<workout_id>/<set_id>/", methods=["POST"])
@login_required
def sets_delete(event_id, workout_id, set_id):
    e = Sets.query.get(set_id)

    db.session.delete(e)
    db.session.commit()

    return redirect(url_for("events_edit", event_id=event_id, workout=workout_id))