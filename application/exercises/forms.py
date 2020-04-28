from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, BooleanField, validators

from application.exercises.models import Exercises

class ExerciseForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(max=144)])
    description = StringField("Kuvaus", [validators.Length(max=144)])
    unit = RadioField('Toistoissa käytetty yksikkö', choices=[('kg','Kilogramma'),('min','Minuutti'),('sec', 'Sekunti'),('m', 'Metri'),('km', 'Kilometri')], default='kg')
    
    class Meta:
        csrf = False

class ExerciseEditForm(FlaskForm):
    name = StringField("Korvaava nimi", [validators.Length(max=144)])
    description = StringField("Korvaava kuvaus", [validators.Length(max=144)])
    unit = RadioField('Korvaava toistoissa käytetty yksikkö', choices=[('kg','Kilogramma'),('min','Minuutti'),('sec', 'Sekunti'),('m', 'Metri'),('km', 'Kilometri')])

    class Meta:
        csrf = False

class ExerciseFilterForm(FlaskForm):
    createdBy = StringField("Lisääjä")

    class Meta:
        csrf = False