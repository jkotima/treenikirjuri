from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField, IntegerField


class ProgramForm(FlaskForm):
    name = StringField("Nimi", [validators.required(),
                                validators.Length(max=144)])

    description = StringField("Kuvaus", [validators.Length(max=144)])

    class Meta:
        csrf = False


class ProgramFilterForm(FlaskForm):
    createdBy = StringField("Lisääjä", [validators.Length(max=144)])

    class Meta:
        csrf = False


class ProgramAddWorkoutForm(FlaskForm):
    name = StringField("Nimi", [validators.required(), 
                                validators.Length(max=144)])

    description = StringField("Kuvaus", [validators.Length(max=144)])

    class Meta:
        csrf = False


class NewSelectField(SelectField):
    # overridetaan Selectfieldin pre_validate -metodi
    # (palauttaa validationerrorin ilman syytä)
    def pre_validate(self, form):
        pass


class AddExerciseToWorkoutForm(FlaskForm):
    exercise = NewSelectField('Harjoitus', coerce=int)
    sets = IntegerField('Sarjat', [validators.required(), 
                                   validators.NumberRange(min=1)])

    reps = IntegerField('Toistot', [validators.required(), 
                                    validators.NumberRange(min=1)])

    class Meta:
        csrf = False
