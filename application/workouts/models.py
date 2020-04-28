from application import db
from application.models import Base
from sqlalchemy.sql import text

# liitostaulu workout_exercise
workout_exercise = db.Table('workout_exercise',
                            db.Column('workout_id', db.Integer,
                                      db.ForeignKey('workouts.id'),
                                      primary_key=True),
                            db.Column('exercise_id', db.Integer,
                                      db.ForeignKey('exercises.id'),
                                      primary_key=True),
                            db.Column('sets', db.Integer),
                            db.Column('reps', db.Integer)
                            )


class Workouts(Base):
    __tablename__ = "workouts"

    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=False)

    program_id = db.Column(db.Integer, db.ForeignKey('programs.id'),
                           nullable=False)

    # workout_exercise
    exercises = db.relationship('Exercises',
                                secondary=workout_exercise,
                                lazy='subquery',
                                backref=db.backref('Workouts', lazy=True))

    def __init__(self, name, description, program_id):
        self.name = name
        self.description = description
        self.program_id = program_id

    # oli pakko tehdä ra'alla sql, koska sets ja reps ei pääse muuten käsiksi
    def add_exercise(self, exercise_id, sets, reps):
        # INSERT or REPLACE INTO toimii sqlitessä, ei postgressa ):
        stmt = text("INSERT INTO workout_exercise "
                    "(workout_id, exercise_id, sets, reps) "
                    "VALUES (:workout_id, :exercise_id, :sets, :reps)"
                    ).params(workout_id=self.id, exercise_id=exercise_id,
                             sets=sets, reps=reps)
        db.engine.execute(stmt)

    def delete_exercise(self, exercise_id):
        stmt = text("DELETE FROM workout_exercise "
                    "WHERE workout_id = :workout_id "
                    "AND exercise_id = :exercise_id"
                    ).params(workout_id=self.id, exercise_id=exercise_id)
        db.engine.execute(stmt)

    def get_exercises(self):
        stmt = text("SELECT workout_id, exercise_id, "
                    "name, sets, reps, description, unit FROM workout_exercise "
                    "LEFT JOIN exercises ON exercise_id = exercises.id "
                    "WHERE workout_id = :workout_id"
                    ).params(workout_id=self.id)

        results = db.engine.execute(stmt)
        r = []
        for row in results:
            r.append({"workout_id": row[0], "id": row[1],
                      "name": row[2], "sets": row[3], "reps": row[4],
                      "description": row[5], "unit": row[6]})

        return r
