from application import db
from application.models import Base

class Events(Base):

    __tablename__ = "events"

    comment = db.Column(db.String(144), nullable=False) 

    sets = db.relationship('Sets', backref='Events', lazy=True)

    user_id = db.Column(db.Integer, db.ForeignKey('accounts.id'),
                        nullable=False)
