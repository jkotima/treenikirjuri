from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, validators

class ExerciseForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=2)])
    description = StringField("Kuvaus")
    unit = RadioField('Toistoissa käytetty yksikkö', choices=[('kg','Kilogramma'),('min','Minuutti'),('sec', 'Sekunti')], default='kg')
    class Meta:
        csrf = False
