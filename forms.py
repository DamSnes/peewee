from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class Validation(FlaskForm):
    name = StringField("name", validators=[DataRequired(), Length(min=1, max=500)])