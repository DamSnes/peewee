from flask import render_template, request, url_for, redirect
from flask_login import current_user, login_user, logout_user
from app.flask import login_manager
from app.models.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from app.flask import app


@login_manager.user_loader
def load_user(id):
    try:
        return User.get(User.id == id)
    except User.DoesNotExist:
        return None


@app.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect('/')

    return render_template('login.html')


@app.route('/login/create', methods=['GET', 'POST'])
def sessions_create():
    print("начало", request.form)
    if request.form.get('email') and request.form.get('password'):

        try:
            user = User.get(User.email == request.form.get('email'))
        except User.DoesNotExist:
            return redirect(url_for('sessions_create'))

        if check_password_hash(user.password, request.form['password']):
            print("пройдено")
            login_user(user)
            return redirect('/')
    return redirect('/')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect('/')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        return render_template('register.html')
    if request.form.get('name') and request.form.get('email') and request.form.get('password'):
        hashing = generate_password_hash(request.form.get('password'))
        User.create(name=request.form.get('name'), email=request.form.get('email'), password=hashing)
        return redirect('/login')

    return redirect('/register')