from . import db
        
class Test(db.Model):
    __tablename__ = "Test"
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime)
    
    def __init__(self, datetime):
        self.datetime = datetime