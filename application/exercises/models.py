from application import db

class Exercise(db.Model):

    __tablename__ = "Exercises"

    id = db.Column(db.Integer, primary_key = True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())
    
    name = db.Column(db.String(144), nullable=False) 
    description = db.Column(db.String(144), nullable=False)
    unit = db.Column(db.String(20), nullable=False)

    created_by = db.Column(db.Integer, db.ForeignKey('Accounts.id'),
                        nullable=False)

    def __init__(self, name):
        self.name = name


