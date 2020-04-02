from flask_wtf import FlaskForm
from wtforms import RadioField, validators, SelectField, FloatField, IntegerField
from application.events.models import Events
from application.exercises.models import Exercises


class AddSetToEventForm(FlaskForm):
    exercise = SelectField('Exercise', coerce=int)
    reps = IntegerField('Reps')
    amount = FloatField("Amount", [validators.required()])

    class Meta:
        csrf = False