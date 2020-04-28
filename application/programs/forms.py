from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, BooleanField, validators, SelectField, IntegerField

class ProgramForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=1, max=144)])
    description = StringField("Kuvaus", [validators.Length(max=144)])
  
    class Meta:
        csrf = False

class ProgramFilterForm(FlaskForm):
    createdBy = StringField("Lisääjä", [validators.Length(max=144)])

    class Meta:
        csrf = False

class ProgramAddWorkoutForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=1, max=144)])
    description = StringField("Kuvaus", [validators.Length(max=144)])

    class Meta:
        csrf = False

# overridetaan Selectfieldin pre_validate -metodi
# (joka palauttaa validationerrorin ilman järkiperäisiä perusteita)
class NewSelectField(SelectField):
    def pre_validate(self, form):
        pass

class AddExerciseToWorkoutForm(FlaskForm):
    exercise = NewSelectField('Harjoitus', coerce=int)
    sets = IntegerField('Sarjat', [validators.NumberRange(min=1)])
    reps = IntegerField('Toistot', [validators.NumberRange(min=1)])
    class Meta:
        csrf = False