from flask_wtf import FlaskForm
from wtforms import validators, SelectField, FloatField, IntegerField, TextAreaField
from application.events.models import Events
from application.exercises.models import Exercises


class AddSetToEventForm(FlaskForm):
    exercise = SelectField('Exercise', coerce=int)
    reps = IntegerField('Reps')
    amount = FloatField("Amount", [validators.required()])

    class Meta:
        csrf = False

class CommentEventForm(FlaskForm):
    comments = TextAreaField('Comments', [validators.optional(), validators.length(max=110)])