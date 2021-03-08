from .. import db
import datetime
from datetime import datetime as dt
from ..config import key


class Transactions(db.Model):
    """ Transaction Model for storing transaction related details """
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    processed_on = db.Column(db.DateTime, nullable=False, default=dt.utcnow)
    house_features = db.Column(db.Integer, db.ForeignKey('houses.id'))

    def __repr__(self):
        return f"<Transaction '{self.id}','{self.processed_on}'>"