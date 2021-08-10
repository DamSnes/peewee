from flask import render_template, request, redirect
from flask_login import login_required
from app.models.models import Expense
from forms import Validation
from app.flask import app


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
    form = Validation()
    return render_template('posts.html', expense=expense, form=form)


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