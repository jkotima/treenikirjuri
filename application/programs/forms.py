from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, BooleanField, validators, SelectField, IntegerField

class ProgramForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=1, max=144)])
    description = StringField("Kuvaus", [validators.Length(max=144)])
  
    class Meta:
        csrf = False

class ProgramFilterForm(FlaskForm):
    createdBy = StringField("Lisääjä")

    class Meta:
        csrf = False

class ProgramAddWorkoutForm(FlaskForm):
    name = StringField("Nimi")
    description = StringField("Kuvaus")

    class Meta:
        csrf = False

class AddExerciseToWorkoutForm(FlaskForm):
    exercise = SelectField('Harjoitus', coerce=int)
    sets = IntegerField('Sarjat')
    reps = IntegerField('Toistot')
    class Meta:
        csrf = False