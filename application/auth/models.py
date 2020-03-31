from application import db
from application.models import Base

#liitostaulu user_program
user_program = db.Table('user_program',
    db.Column('user_id', db.Integer, db.ForeignKey('accounts.id'), primary_key=True),
    db.Column('program_id', db.Integer, db.ForeignKey('programs.id'), primary_key=True)
)

class Users(Base):

    __tablename__ = "accounts"
  
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    exercises = db.relationship('Exercises', backref='Accounts', lazy=True)
    events = db.relationship('Events', backref='Accounts', lazy=True)
    programs = db.relationship('Programs', backref='Accounts', lazy=True)

    #user_program
    programs = db.relationship('Programs', secondary=user_program, lazy='subquery',
        backref=db.backref('Users', lazy=True))    

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
