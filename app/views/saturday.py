from flask import render_template, redirect, session, request
from app.models.models import Saturday, HEADINGS_TABLE
from forms import Validation
from app.flask import app


@app.route('/table/saturday', methods=['POST', 'GET'])
def saturday():

    bring = Saturday.select()
    form = Validation()

    return render_template('saturday.html', form=form, headings_table=HEADINGS_TABLE, bring=bring)


@app.route('/table/saturday/edit', methods=['POST'])
def saturday_edit():

    if request.form.get('time') and request.form.get('subject') and request.form.get('auditorium'):
        Saturday.create(time=request.form.get('time'), subject=request.form.get('subject'), auditorium=request.form.get('auditorium'))
        print("ok")

    print("create_saturday")

    return redirect('/table/saturday')


@app.route('/table/saturday/delete/<int:id>', methods=['POST', 'GET', 'DELETE'])
def saturday_delete(id):

    delete = Saturday.delete().where(Saturday.id == id).execute()
    print("delete")
    try:
        return redirect('/table/saturday')
    except:
        return "Ошибка при удалении"

    return render_template('saturday.html', delete=delete)
