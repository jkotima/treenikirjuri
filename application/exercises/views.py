from application import app, db
from flask import render_template, request, url_for, redirect
from application.exercises.models import Exercise

@app.route("/exercises", methods=["GET"])
def exercises_index():
    return render_template("exercises/list.html", exercises = Exercise.query.all())

@app.route("/exercises/new/")
def exercises_form():
    return render_template("exercises/new.html")

@app.route("/exercises/delete/<exercise_id>/", methods=["POST"])
def exercises_delete(exercise_id):   
    e = Exercise.query.get(exercise_id)

    db.session.delete(e)
    db.session.commit()

    return redirect(url_for("exercises_index"))

@app.route("/exercises/", methods=["POST"])
def exercises_create():
    e = Exercise(request.form.get("name"))

    db.session().add(e)
    db.session().commit()

    return redirect(url_for("exercises_index"))


