from .. import db
import datetime
from ..config import key


class Houses(db.Model):
    """ House Model for storing house features """
    __tablename__ = "houses"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    crim = db.Column(db.Float,nullable=False)
    zn = db.Column(db.Float,nullable=False)
    indus = db.Column(db.Float,nullable=False)
    chas = db.Column(db.Float,nullable=False)
    nox = db.Column(db.Float,nullable=False)
    rm = db.Column(db.Float,nullable=False)
    age = db.Column(db.Float,nullable=False)
    dis = db.Column(db.Float,nullable=False)
    rad = db.Column(db.Float,nullable=False)
    tax = db.Column(db.Float,nullable=False)
    ptratio =  db.Column(db.Float,nullable=False)
    b = db.Column(db.Float,nullable=False)
    lstat = db.Column(db.Float,nullable=False)
    
    transaction = db.relationship("Transactions",  backref="for_house")
    
    def __repr__(self):
        return f"<Transaction '{self.id}','{self.processed_on}'>"