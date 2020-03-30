from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, validators

from application.exercises.models import Exercises


class ExerciseForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=2)])
    description = StringField("Kuvaus")
    unit = RadioField('Toistoissa käytetty yksikkö', choices=[('kg','Kilogramma'),('min','Minuutti'),('sec', 'Sekunti')], default='kg')
    class Meta:
        csrf = False

class ExerciseEditForm(FlaskForm):
    name = StringField("Korvaava nimi", [validators.Length(min=2)])
    description = StringField("Korvaava kuvaus")
    unit = RadioField('Korvaava toistoissa käytetty yksikkö', choices=[('kg','Kilogramma'),('min','Minuutti'),('sec', 'Sekunti')])

    class Meta:
        csrf = False