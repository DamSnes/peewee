from flask import render_template, redirect, session, request
from app.models.models import Thursday, HEADINGS_TABLE
from forms import Validation
from app.flask import app


@app.route('/table/thursday', methods=['POST', 'GET'])
def thursday():

    bring = Thursday.select()
    form = Validation()

    return render_template('thursday.html', form=form, headings_table=HEADINGS_TABLE, bring=bring)


@app.route('/table/thursday/edit', methods=['POST'])
def thursday_edit():

    if request.form.get('time') and request.form.get('subject') and request.form.get('auditorium'):
        Thursday.create(time=request.form.get('time'), subject=request.form.get('subject'), auditorium=request.form.get('auditorium'))
        print("ok")

    print("create_thursday")

    return redirect('/table/thursday')


@app.route('/table/thursday/delete/<int:id>', methods=['POST', 'GET', 'DELETE'])
def thursday_delete(id):

    delete = Thursday.delete().where(Thursday.id == id).execute()
    print("delete")
    try:
        return redirect('/table/thursday')
    except:
        return "Ошибка при удалении"

    return render_template('thursday.html', delete=delete)
