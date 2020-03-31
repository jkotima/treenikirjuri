from application import db
from application.models import Base

class programs(Base):

    __tablename__ = "programs"

    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=False)

    created_by = db.Column(db.Integer, db.ForeignKey('accounts.id'),
                    nullable=False)
