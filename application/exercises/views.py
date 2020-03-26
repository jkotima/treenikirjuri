from application import app, db
from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user
from application.exercises.models import Exercise
from application.exercises.forms import ExerciseForm

@app.route("/exercises", methods=["GET"])
@login_required
def exercises_index():
    return render_template("exercises/list.html", exercises = Exercise.query.all())

@app.route("/exercises/new/")
@login_required
def exercises_form():
    return render_template("exercises/new.html", form = ExerciseForm())

@app.route("/exercises/delete/<exercise_id>/", methods=["POST"])
@login_required
def exercises_delete(exercise_id):   
    e = Exercise.query.get(exercise_id)

    db.session.delete(e)
    db.session.commit()

    return redirect(url_for("exercises_index"))

@app.route("/exercises/", methods=["POST"])
@login_required
def exercises_create():
    form = ExerciseForm(request.form)

    if not form.validate():
        return render_template("exercises/new.html", form = form)

    e = Exercise(form.name.data)
    e.description = form.description.data
    e.unit = form.unit.data
    e.created_by = current_user.id

    db.session().add(e)
    db.session().commit()

    return redirect(url_for("exercises_index"))


