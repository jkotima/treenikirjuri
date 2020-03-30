from application import db
from application.models import Base

class Exercises(Base):

    __tablename__ = "Exercises"

    name = db.Column(db.String(144), nullable=False) 
    description = db.Column(db.String(144), nullable=False)
    unit = db.Column(db.String(20), nullable=False)

    created_by = db.Column(db.Integer, db.ForeignKey('Accounts.id'),
                        nullable=False)

    def __init__(self, name):
        self.name = name