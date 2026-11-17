from flask import Flask, render_tempates, redirect, url_for, flash, request
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from extensions import db
from models import Users


app = Flask(__name__)

app.config['SECRET_KEY'] = 'BALDBALD'
app.config['SQLALCHEMY_DATEBASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

with app.app_context():
    db.create_all()


@app.route('/login')
def login():
    return render_tempates('login.html')

@app.route('/index')
def index():
    return render_tempates('index.html')

@app.route('/rooms')
def login():
    return render_tempates('rooms.html')