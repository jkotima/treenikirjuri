from application import db
from application.models import Base
from sqlalchemy.sql import text

class Sets(Base):
    __tablename__ = "sets"

    reps = db.Column(db.Integer)
    amount = db.Column(db.Float, nullable=False)

    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'),
                        nullable=False)

    event_id = db.Column(db.Integer, db.ForeignKey('events.id'),
                        nullable=False)

    def __init__(self, reps, amount, exercise_id, event_id):
        self.reps = reps
        self.amount = amount
        self.exercise_id = exercise_id
        self.event_id = event_id
    
    @staticmethod
    def find_sets_by_event_id(event_id):
        stmt = text("SELECT exercises.name, sets.reps, sets.amount, exercises.unit, sets.id FROM exercises"
                    " LEFT JOIN sets ON exercise_id = exercises.id"
                    " WHERE event_id = :id").params(id=event_id)
                    

        results = db.engine.execute(stmt)
        r = []
        for row in results:
            r.append({"exercise":row[0], "reps":row[1], "amount":row[2], "unit":row[3], "id":row[4]})

        return r
    
    @staticmethod
    def find_total_lifted(user_id):
        stmt = text("SELECT SUM(sets.reps*sets.amount) AS weight FROM sets"
                    " LEFT JOIN exercises ON sets.exercise_id = exercises.id"
                    " LEFT JOIN events ON sets.event_id = events.id"
                    " WHERE exercises.unit = 'kg' AND events.user_id = :id").params(id=user_id)

        result = db.engine.execute(stmt).fetchone().weight
        return result