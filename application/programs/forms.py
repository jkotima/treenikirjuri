from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, BooleanField, validators

class ProgramForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=2, max=144)])
    description = StringField("Kuvaus", [validators.Length(max=144)])
  
    class Meta:
        csrf = False

class ProgramFilterForm(FlaskForm):
    createdBy = StringField("Lisääjä")

    class Meta:
        csrf = False