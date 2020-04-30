from flask_wtf import FlaskForm
from wtforms import (validators, SelectField, FloatField, IntegerField,
                     TextAreaField)


class AddSetToEventForm(FlaskForm):
    amount = FloatField("Amount", [validators.required(),
                                   validators.NumberRange(min=0,
                                                          max=1000000000)])

    class Meta:
        csrf = False


class NewSelectField(SelectField):
    # overridetaan Selectfieldin pre_validate -metodi
    # (palauttaa validationerrorin ilman syytä)
    def pre_validate(self, form):
        pass


class AddCustomSetToEventForm(FlaskForm):
    exercise = NewSelectField('Exercise', coerce=int)
    reps = IntegerField('Reps', [validators.required(), 
                                 validators.NumberRange(min=1, 
                                                        max=1000000000)])

    amount = FloatField("Amount", [validators.required(), 
                                   validators.NumberRange(min=0, 
                                                          max=1000000000)])

    class Meta:
        csrf = False


class CommentEventForm(FlaskForm):
    comments = TextAreaField('Comments',
                             [validators.optional(),
                              validators.Length(max=144)])

    class Meta:
        csrf = False


class SelectWorkoutForm(FlaskForm):
    workout = SelectField('Exercise', coerce=int)

    class Meta:
        csrf = False
