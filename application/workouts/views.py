from application import app, db
from flask import request, url_for, redirect
from flask_login import login_required, current_user
from application.workouts.models import Workouts
from application.exercises.models import Exercises
from application.programs.models import Programs

from application.programs.forms import AddExerciseToWorkoutForm


@app.route("/workouts/delete/<program_id>/<workout_id>/", methods=["POST"])
@login_required
def workouts_delete(program_id, workout_id):
    # authorization
    if Programs.query.get(program_id).created_by != current_user.id:
        return redirect(url_for("programs_index"))

    wo = Workouts.query.get(workout_id)

    db.session.delete(wo)
    db.session.commit()

    # delete references in workout_exercise (if any)
    wo.delete_references()

    return redirect(url_for("programs_edit", program_id=program_id))


@app.route("/workouts/addExercise/<program_id>/<workout_id>/",
           methods=["POST"])
@login_required
def workouts_add_exercise(program_id, workout_id):
    form = AddExerciseToWorkoutForm(request.form)

    # authorization
    if Programs.query.get(program_id).created_by != current_user.id:
        return redirect(url_for("programs_index"))

    if not form.validate():
        return redirect(url_for("programs_edit", program_id=program_id))
        pass

    wo = Workouts.query.get(workout_id)
    e = Exercises.query.get(form.exercise.data)
    wo.add_exercise(e.id, form.sets.data, form.reps.data)

    return redirect(url_for("programs_edit", program_id=program_id))


@app.route("/workouts/deleteExercise/<program_id>/<workout_id>/<exercise_id>",
           methods=["POST"])
@login_required
def workouts_delete_exercise(program_id, workout_id, exercise_id):

    # authorization
    if Programs.query.get(program_id).created_by != current_user.id:
        return redirect(url_for("programs_index"))

    wo = Workouts.query.get(workout_id)
    wo.delete_exercise(exercise_id)

    return redirect(url_for("programs_edit", program_id=program_id))