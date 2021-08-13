from flask import render_template, request, redirect
from flask_login import current_user, login_required
from app.models.models import Message, User, HEADINGS_MESSAGES
from forms import Validation
from app.flask import app


@app.route('/chat', methods=['POST'])
@login_required
def create_chat():

    form = Validation()

    if form.validate_on_submit():
        Message.create(message=form.name.data, user=current_user)
        print("ok")

    print("create_message")

    return redirect('/chat')


@app.route('/chat', methods=['GET'])
@login_required
def chat():


    # # bring = Expense.select().where(User.user==current_user).order_by(Expense.id.asc())
    bring = Message.select()
    form = Validation()

    return render_template('chat.html', form=form, headings_messages=HEADINGS_MESSAGES, bring=bring)


@app.route('/chat/clear', methods=['POST'])
@login_required
def clear_chat():

    clear = Message.delete().execute()
    print("clear")
    try:
        return redirect('/')
    except:
        return "Ошибка при удалении"

    return render_template('chat.html', clear=clear)

    return redirect('/chat')