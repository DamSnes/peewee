from flask import render_template, redirect, session, request
from app.models.models import Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, HEADINGS_TABLE
from forms import Validation
from app.flask import app


@app.route('/table', methods=['GET', 'POST'])
def table():

    мonday_bring = Monday.select()
    tuesday_bring = Tuesday.select()
    wednesday_bring = Wednesday.select()
    thursday_bring = Thursday.select()
    friday_bring = Friday.select()
    saturday_bring = Saturday.select()

    form = Validation()

    return render_template('table.html', form=form, мonday_bring=мonday_bring, tuesday_bring=tuesday_bring, wednesday_bring=wednesday_bring, thursday_bring=thursday_bring, friday_bring=friday_bring, saturday_bring=saturday_bring, headings_table=HEADINGS_TABLE)


