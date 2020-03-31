from application import db
from application.models import Base

#liitostaulu workout_exercise
workout_exercise = db.Table('workout_exercise',
    db.Column('workout_id', db.Integer, db.ForeignKey('workouts.id'), primary_key=True),
    db.Column('exercise_id', db.Integer, db.ForeignKey('exercises.id'), primary_key=True)
)

class Workouts(Base):

    __tablename__ = "workouts"

    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=False)

    program_id = db.Column(db.Integer, db.ForeignKey('programs.id'),
                    nullable=False)

    #workout_exercise
    exercises = db.relationship('Exercises', secondary=workout_exercise, lazy='subquery',
        backref=db.backref('Workouts', lazy=True))  