from . import db
        
class History(db.Model):
    __tablename__ = "HISTORY"
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime)
    
    def __init__(self, datetime):
        self.datetime = datetime