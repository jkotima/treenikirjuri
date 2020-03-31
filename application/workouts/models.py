from application import db
from application.models import Base

class Workouts(Base):

    __tablename__ = "workouts"

    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=False)

    program_id = db.Column(db.Integer, db.ForeignKey('programs.id'),
                    nullable=False)
    