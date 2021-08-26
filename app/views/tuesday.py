from flask import render_template, redirect, session, request
from app.models.models import Tuesday, HEADINGS_TABLE
from forms import Validation
from app.flask import app


@app.route('/table/tuesday', methods=['POST', 'GET'])
def tuesday():

    bring = Tuesday.select()
    form = Validation()

    return render_template('tuesday.html', form=form, headings_table=HEADINGS_TABLE, bring=bring)


@app.route('/table/tuesday/edit', methods=['POST'])
def tuesday_edit():

    if request.form.get('time') and request.form.get('subject') and request.form.get('auditorium'):
        Tuesday.create(time=request.form.get('time'), subject=request.form.get('subject'), auditorium=request.form.get('auditorium'))
        print("ok")

    print("create_tuesday")

    return redirect('/table/tuesday')


@app.route('/table/tuesday/delete/<int:id>', methods=['POST', 'GET', 'DELETE'])
def tuesday_delete(id):

    delete = Tuesday.delete().where(Tuesday.id == id).execute()
    print("delete")
    try:
        return redirect('/table/tuesday')
    except:
        return "Ошибка при удалении"

    return render_template('tuesday.html', delete=delete)
