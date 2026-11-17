from datetime import datetime
from extensions import db
from flask_login import UserMixin

class Users(db.Model, UserMixin):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(80), unique=True ,nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(50), default='user', nullable=False)


