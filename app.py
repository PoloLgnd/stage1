from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from extensions import db
from models import Users


app = Flask(__name__)

app.config['SECRET_KEY'] = 'BALDBALD'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


with app.app_context():
    db.create_all()


# ---------- Маршруты ----------

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_val = request.form.get('login', '').strip()
        user = Users.query.filter_by(username=login_val).first()
        if user:
            login_user(user)
            if user.role == 'admin':
                return redirect(url_for('admin'))
            return redirect(url_for('cabinet'))
        flash('Вход выполнен', 'success')
        return redirect(url_for('cabinet'))
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        flash('Пользователь создан. Теперь войдите в систему.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/rooms', methods=['GET', 'POST'])
@app.route('/booking/new', methods=['GET', 'POST'])
def rooms():
    if request.method == 'POST':
        flash('Заявка отправлена администратору', 'success')
        return redirect(url_for('cabinet'))
    return render_template('rooms.html')


@app.route('/booking_new')
def booking_new():
    return render_template('booking_new.html')


@app.route('/cabinet')
def cabinet():
    return render_template('cabinet.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


# Простые заглушки для действий на кнопках
@app.route('/booking/<int:booking_id>/delete', methods=['POST'])
def booking_delete(booking_id):
    flash('Заявка удалена', 'success')
    return redirect(url_for('cabinet'))


@app.route('/booking/<int:booking_id>/review', methods=['POST'])
def booking_review(booking_id):
    flash('Спасибо за отзыв!', 'success')
    return redirect(url_for('cabinet'))


@app.route('/admin/booking/<int:booking_id>/status', methods=['POST'])
def admin_change_status(booking_id):
    flash('Статус изменён', 'success')
    return redirect(url_for('admin'))


@app.route('/admin/booking/<int:booking_id>/delete', methods=['POST'])
def admin_delete(booking_id):
    flash('Заявка удалена', 'success')
    return redirect(url_for('admin'))


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
