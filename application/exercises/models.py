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

    def __init__(self, name):
        self.name = name

    def get_creators_name(self):
        a = Users.query.get(self.created_by)
        return a.name