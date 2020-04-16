from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjänimi")
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=2, max=144)])
    username = StringField("Käyttäjänimi", [validators.Length(min=2, max=144)])
    password = PasswordField("Salasana", [validators.Length(min=2, max=144)])
  
    class Meta:
        csrf = False        