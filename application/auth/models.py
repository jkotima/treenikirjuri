from application import db
from application.models import Base
from application.programs.models import Programs

class Users(Base):

    __tablename__ = "accounts"
  
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    exercises = db.relationship('Exercises', backref='Users', lazy=True)
    events = db.relationship('Events', backref='Users', lazy=True)
    #programs = db.relationship('Programs', backref='Users', lazy=True)
    
    active_program = db.Column(db.Integer, db.ForeignKey('programs.id'),
                        nullable=True)

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

    def get_active_program(self):
        return Programs.query.get(self.active_program)

    def get_active_program_name(self):
        if self.get_active_program():
            return self.get_active_program().name
        else:
            return None