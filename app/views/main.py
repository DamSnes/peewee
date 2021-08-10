from flask import render_template, redirect, session
from flask_login import current_user, login_required
from app.models.models import Expense, User, HEADLINGS
from forms import Validation
from app.flask import app


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

    return render_template('index.html', number=number, user_count=user_count, filter=filter, bring=bring, form=form, headings=HEADLINGS)