from flask import Flask, render_template, request, url_for, redirect, session, g, make_response
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user
from models import Expense, User
from forms import Validation
import hashlib



#from app import app, db, root, login_manager
import re


app = Flask(__name__, static_folder='')
app.config['SECRET_KEY'] = 'key'
login_manager = LoginManager()
login_manager.init_app(app)


headings = ("Id", "Name", "Date", "Edit")
data = ()


@app.route('/', methods=['POST'])
def create():

    form = Validation()

    if form.validate_on_submit():
        Expense.create(name=form.name.data)
        print("ok")

    print("create")

    return redirect('/')


@app.route('/', methods=['GET'])
def index():

    filter = {}
    bring = Expense.select().order_by(Expense.id.asc())
    form = Validation()

    for number in enumerate(bring, 1):

        print(number)

    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1
    print(session)

    return render_template('index.html', number=number, filter=filter, bring=bring, form=form, headings=headings, data=data)


@app.route('/delete', methods=['POST', 'GET', 'DELETE'])
def delete_all():

    delete = Expense.delete().execute()
    print("delete")
    try:
        return redirect('/')
    except:
        return "Ошибка при удалении"

    return render_template('index.html', delete_all=delete_all)


@app.route('/delete/<int:id>', methods=['POST', 'GET', 'DELETE'])
def delete(id):

    delete = Expense.delete().where(Expense.id == id).execute()
    print("delete")
    try:
        return redirect('/')
    except:
        return "Ошибка при удалении"

    return render_template('index.html', delete=delete)


@app.route('/posts/<int:id>', methods=['POST', 'GET'])
def update(id):

    expense = Expense.get(Expense.id == id)
    return render_template('posts.html', expense=expense)


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


# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     return render_template('login.html')


# @app.route('/register', methods=['POST', 'GET'])
# def register():
#     return render_template('register.html')


# @app.route('/login', methods=['POST', 'GET'])
# def create_cookie():
#     log = ""
#     if request.cookies.get('logged'):
#         log = request.cookies.get('logged')
#
#     res = make_response(f"<h1>Авторизация</h1><p>logged: {log}")
#     res.set_cookie("logged", "yes")
#     return res
#
#
# @app.route('/logout', methods=['POST', 'GET'])
# def delete_cookie():
#     res = make_response(f"<h1>Вы не авторизованны !</h1>")
#     res.set_cookie("logged", "", 0)
#     return res


@login_manager.user_loader
def load_user(id):
    try:
        return User.get(User.id == int(id))
    except User.DoesNotExist:
        return None


@app.route('/login')
def sessions_new():
    if current_user.is_authenticated:
        return redirect('/')

    return render_template('login.html')


@app.route('/login/create', methods=['POST'])
def sessions_create():
    # if request.form.get('user[login]') and request.form.get('user[password]'):
    #
    #     try:
    #         user = User.get(User.username == request.form.get('user[login]'))
    #     except User.DoesNotExist:
    #         return redirect(url_for('sessions_new'))
    #
    #     if user.authenticate(request.form['user[password]']):
    #
    #         login_user(user)
    #         return redirect(url_for('admins_main_index'))

    return render_template('login.html')


@app.route('/login/delete', methods=['POST'])
def sessions_delete():
    logout_user()

    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

