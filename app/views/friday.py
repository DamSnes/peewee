from flask import render_template, redirect, session, request
from app.models.models import Friday, HEADINGS_TABLE
from forms import Validation
from app.flask import app


@app.route('/table/friday', methods=['POST', 'GET'])
def friday():

    bring = Friday.select()
    form = Validation()

    return render_template('friday.html', form=form, headings_table=HEADINGS_TABLE, bring=bring)


@app.route('/table/friday/edit', methods=['POST'])
def friday_edit():

    if request.form.get('time') and request.form.get('subject') and request.form.get('auditorium'):
        Friday.create(time=request.form.get('time'), subject=request.form.get('subject'), auditorium=request.form.get('auditorium'))
        print("ok")

    print("create_friday")

    return redirect('/table/friday')


@app.route('/table/friday/delete/<int:id>', methods=['POST', 'GET', 'DELETE'])
def friday_delete(id):

    delete = Friday.delete().where(Friday.id == id).execute()
    print("delete")
    try:
        return redirect('/table/friday')
    except:
        return "Ошибка при удалении"

    return render_template('friday.html', delete=delete)
