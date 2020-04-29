from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjänimi")
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=3, max=30)])
    username = StringField("Käyttäjänimi", [validators.Length(min=3, max=30)])
    password = PasswordField("Salasana", [validators.Length(min=3, max=30)])
  
    class Meta:
        csrf = False        