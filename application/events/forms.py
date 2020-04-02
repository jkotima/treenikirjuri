from flask_wtf import FlaskForm
from wtforms import RadioField, validators, SelectField, FloatField, IntegerField
from application.events.models import Events
from application.exercises.models import Exercises


class AddSetToEventForm(FlaskForm):
    exercises = Exercises.query.all()
    c = []

    for exercise in exercises:
        c.append((exercise.id, exercise.name))

    exercise = SelectField('Exercise', choices=c)
    reps = IntegerField('Reps')
    amount = FloatField("Amount", [validators.required()])

    class Meta:
        csrf = False