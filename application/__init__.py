# flask
from flask import Flask
app = Flask(__name__)

# tietokanta
from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///exercises.db"    
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# sovelluksen toiminnallisuudet


from application.exercises import models
from application.auth import models
from application.programs import models
from application.sets import models
from application.workouts import models
from application.events import models

#luodaan taulut tietokantaan tarvittaessa
try: 
    db.create_all()
except:
    pass


# kirjautuminen
from application.auth.models import Users
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

# näkymät
from application import views
from application.exercises import views
from application.auth import views
from application.events import views
from application.sets import views
from application.programs import views
