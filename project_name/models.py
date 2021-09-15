from . import db
        
class Test(db.Model):
    __tablename__ = "Test"
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime)
    
    def __init__(self, datetime):
        self.datetime = datetime
        
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(10))
    pw = db.Column(db.String(30))
    
    def __init__(self, user_id, pw):
        self.user_id = user_id
        self.pw = pw