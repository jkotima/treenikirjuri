from application import db
from application.models import Base
from sqlalchemy.sql import text
from application.auth.models import Users


class Exercises(Base):

    __tablename__ = "exercises"

    name = db.Column(db.String(144), nullable=False) 
    description = db.Column(db.String(144), nullable=False)
    unit = db.Column(db.String(20), nullable=False)

    created_by = db.Column(db.Integer, db.ForeignKey('accounts.id'),
                        nullable=False)

    sets = db.relationship('Sets', backref='Exercises', lazy=True)

    def __init__(self, name):
        self.name = name

    def get_creators_name(self):
        c = Users.query.get(self.created_by)
        return c.name

    @staticmethod
    def find_exercises_by_creators_name(created_by):
        stmt = text("SELECT exercises.id, exercises.name, exercises.description, accounts.name AS creators_name FROM exercises"
                    " LEFT JOIN accounts ON created_by = accounts.id"
                    " WHERE accounts.name"
                    " LIKE :name").params(name=created_by+"%")

        return db.engine.execute(stmt)