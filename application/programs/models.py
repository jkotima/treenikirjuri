from application import db
from application.models import Base
from sqlalchemy.sql import text

class Programs(Base):

    __tablename__ = "programs"

    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=False)

    created_by = db.Column(db.Integer, db.ForeignKey('accounts.id'),
                    nullable=False)

    #users = db.relationship('Users', backref='Programs', lazy=True)

    def __init__(self, user_id, name, description):
        self.created_by = user_id
        self.name = name
        self.description = description

    # set active_program null from those users having selected this
    # as active_program
    def set_references_null(self):
        stmt = text("UPDATE accounts SET active_program = NULL"
                    " WHERE active_program = :id").params(id=self.id)        
        db.engine.execute(stmt)

    @staticmethod
    def find_programs_by_creators_name(created_by):
        stmt = text("SELECT programs.id, programs.name, programs.description, accounts.name, programs.created_by FROM programs"
                    " LEFT JOIN accounts ON created_by = accounts.id"
                    " WHERE LOWER(accounts.name)"
                    " LIKE :name").params(name=created_by+"%")
                    
        results = db.engine.execute(stmt)
        r = []
        for row in results:
            r.append({"id":row[0], "name":row[1], "description":row[2], "creators_name":row[3], "created_by":row[4]})

        return r