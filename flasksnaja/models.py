from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) # unique = True กันคนซ้ำ
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    pic = db.Column(db.String(250))
    


