from application import db
from application.models import Base
"""
users = db.Table('UserProgram',
    db.Column('user_id', db.Integer, db.ForeignKey('accounts.id'), primary_key=True),
    db.Column('program_id', db.Integer, db.ForeignKey('programs.id'), primary_key=True)
)
"""
class Programs(Base):

    __tablename__ = "programs"

    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=False)

    #users = db.relationship('Accounts', secondary=users, lazy='subquery',
    #    backref=db.backref('Programs', lazy=True))

    created_by = db.Column(db.Integer, db.ForeignKey('accounts.id'),
                    nullable=False)
