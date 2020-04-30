from application import app, db
from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user
from application.exercises.models import Exercises
from application.exercises.forms import (ExerciseForm, ExerciseEditForm,
                                         ExerciseFilterForm)
from application.sets.models import Sets


@app.route("/exercises", methods=["GET"])
@login_required
def exercises_index():
    created_by = request.args.get('createdBy')

    if (created_by is None):
        e = Exercises.find_exercises_by_creators_name("")
    else:
        e = Exercises.find_exercises_by_creators_name(created_by)

    return render_template("exercises/list.html",
                           exercises=e,
                           form=ExerciseFilterForm())


@app.route("/exercises/new/")
@login_required
def exercises_form():
    return render_template("exercises/new.html", form=ExerciseForm())


@app.route("/exercises/delete/<exercise_id>/", methods=["POST"])
@login_required
def exercises_delete(exercise_id):
    e = Exercises.query.get(exercise_id)

    # authorization
    if e.created_by != current_user.id:
        return redirect(url_for("exercises_index"))

    # delete all sets of this exercise
    Sets.query.filter_by(exercise_id=exercise_id).delete()

    db.session.delete(e)
    db.session.commit()

    return redirect(url_for("exercises_index"))


@app.route("/exercises/edit/<exercise_id>/", methods=["GET"])
@login_required
def exercises_edit(exercise_id):
    e = Exercises.query.get(exercise_id)

    # authorization
    if e.created_by != current_user.id:
        return redirect(url_for("exercises_index"))

    return render_template("exercises/edit.html",
                           form=ExerciseEditForm(),
                           exercise=e)


@app.route("/exercises/edit/<exercise_id>/", methods=["POST"])
@login_required
def exercises_update(exercise_id):
    form = ExerciseEditForm(request.form)
    e = Exercises.query.get(exercise_id)

    if not form.validate():
        return render_template("exercises/edit.html",
                               form=form,
                               exercise=e)

    # authorization
    if e.created_by != current_user.id:
        return redirect(url_for("exercises_index"))

    if form.name.data != "":
        e.name = form.name.data

    if form.description.data != "":
        e.description = form.description.data

    if form.unit.data != "None":
        e.unit = form.unit.data

    db.session().add(e)
    db.session().commit()

    return redirect(url_for("exercises_index"))


@app.route("/exercises/", methods=["POST"])
@login_required
def exercises_create():
    form = ExerciseForm(request.form)

    if not form.validate():
        return render_template("exercises/new.html", form=form)

    e = Exercises(form.name.data)
    e.description = form.description.data
    e.unit = form.unit.data
    e.created_by = current_user.id

    db.session().add(e)
    db.session().commit()

    return redirect(url_for("exercises_index"))
