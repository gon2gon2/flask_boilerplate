from . import db

class User(db.Model):
    __tablename__ = "USER"
    id = db.Column(db.Integer, nullable=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password 