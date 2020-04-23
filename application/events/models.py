from application import db
from application.models import Base
from application.auth.models import Users

class Events(Base):

    __tablename__ = "events"

    comment = db.Column(db.String(144)) 

    sets = db.relationship('Sets', backref='Events', lazy=True)

    user_id = db.Column(db.Integer, db.ForeignKey('accounts.id'),
                        nullable=False)
    
    users = db.relationship('Users', backref='Events', lazy=True)
    
    def __init__(self, user_id):
        self.user_id = user_id

    def get_users_name(self):
        return Users.query.get(self.user_id).name
