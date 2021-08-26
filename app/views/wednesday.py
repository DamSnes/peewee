from flask import render_template, redirect, session, request
from app.models.models import Wednesday, HEADINGS_TABLE
from forms import Validation
from app.flask import app


@app.route('/table/wednesday', methods=['POST', 'GET'])
def wednesday():

    bring = Wednesday.select()
    form = Validation()

    return render_template('wednesday.html', form=form, headings_table=HEADINGS_TABLE, bring=bring)


@app.route('/table/wednesday/edit', methods=['POST'])
def wednesday_edit():

    if request.form.get('time') and request.form.get('subject') and request.form.get('auditorium'):
        Wednesday.create(time=request.form.get('time'), subject=request.form.get('subject'), auditorium=request.form.get('auditorium'))
        print("ok")

    print("create_wednesday")

    return redirect('/table/wednesday')


@app.route('/table/wednesday/delete/<int:id>', methods=['POST', 'GET', 'DELETE'])
def wednesday_delete(id):

    delete = Wednesday.delete().where(Wednesday.id == id).execute()
    print("delete")
    try:
        return redirect('/table/wednesday')
    except:
        return "Ошибка при удалении"

    return render_template('wednesday.html', delete=delete)
