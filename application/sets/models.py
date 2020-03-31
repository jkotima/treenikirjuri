from application import db
from application.models import Base

class Sets(Base):

    __tablename__ = "sets"

    reps = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)

    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'),
                        nullable=False)

    event_id = db.Column(db.Integer, db.ForeignKey('events.id'),
                        nullable=False)
