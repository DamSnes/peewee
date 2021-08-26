from flask import render_template, redirect, session, request
from app.models.models import Monday, HEADINGS_TABLE
from forms import Validation
from app.flask import app


@app.route('/table/monday', methods=['POST', 'GET'])
def monday():

    bring = Monday.select()
    form = Validation()

    return render_template('monday.html', form=form, headings_table=HEADINGS_TABLE, bring=bring)


@app.route('/table/monday/edit', methods=['POST'])
def monday_edit():

    if request.form.get('time') and request.form.get('subject') and request.form.get('auditorium'):
        Monday.create(time=request.form.get('time'), subject=request.form.get('subject'), auditorium=request.form.get('auditorium'))
        print("ok")

    print("create_monday")

    return redirect('/table/monday')


@app.route('/table/monday/delete/<int:id>', methods=['POST', 'GET', 'DELETE'])
def monday_delete(id):

    delete = Monday.delete().where(Monday.id == id).execute()
    print("delete")
    try:
        return redirect('/table/monday')
    except:
        return "Ошибка при удалении"

    return render_template('monday.html', delete=delete)
