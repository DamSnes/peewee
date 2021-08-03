from flask import Flask, render_template, request, url_for, redirect, session, g, make_response
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
from models import Expense, User
from forms import Validation, LoginForm
import hashlib

#from app import app, db, root, login_manager
import re

app = Flask(__name__, static_folder='')
app.config['SECRET_KEY'] = 'key'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

headings = ("Id", "Name", "Date", "Edit")
data = ()


@app.route('/', methods=['POST'])
@login_required
def create():

    form = Validation()

    if form.validate_on_submit():
        Expense.create(name=form.name.data, user=current_user)
        print("ok")

    print("create")

    return redirect('/')


@app.route('/', methods=['GET'])
@login_required
def index():

    filter = {}
    # bring = Expense.select().where(User.user==current_user).order_by(Expense.id.asc())
    bring = current_user.expenses
    form = Validation()
    number = bring.count()
    user_count = User.select().count()

    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1
    print(session)

    return render_template('index.html', number=number, user_count=user_count, filter=filter, bring=bring, form=form, headings=headings, data=data)


@login_required
@app.route('/delete', methods=['POST', 'GET', 'DELETE'])
def delete_all():

    delete = Expense.delete().execute()
    print("delete")
    try:
        return redirect('/')
    except:
        return "Ошибка при удалении"

    return render_template('index.html', delete_all=delete_all)


@login_required
@app.route('/delete/<int:id>', methods=['POST', 'GET', 'DELETE'])
def delete(id):

    delete = Expense.delete().where(Expense.id == id).execute()
    print("delete")
    try:
        return redirect('/')
    except:
        return "Ошибка при удалении"

    return render_template('index.html', delete=delete)


@login_required
@app.route('/posts/<int:id>', methods=['POST', 'GET'])
def update(id):

    expense = Expense.get(Expense.id == id)
    return render_template('posts.html', expense=expense)


@login_required
@app.route('/posts/<int:id>/update', methods=['POST', 'GET'])
def post_update(id):

    expense = Expense.get(Expense.id == id)
    print(request.form)
    expense.name = request.form['name']
    expense.save()

    try:
        return redirect('/')
    except:
        return "Ошибка при изменении"


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

        if user.password == request.form['password']:
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
        User.create(name=request.form.get('name'), email=request.form.get('email'), password=request.form.get('password'))
        return redirect('/login')

    return redirect('/register')


@app.route('/account_delete', methods=['GET', 'POST'])
def account_delete(id):

    User.delete().where(User.id == id).execute()
    print("delete account")

    return redirect('/login')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)