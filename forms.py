from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, Length

class Validation(FlaskForm):
    name = StringField("name", validators=[DataRequired(), Length(min=1, max=500)])
    # email = StringField("Email: ", validators=[Email()])
    # psw = PasswordField("Password: ", validators=[DataRequired(), Length(min=1, max=100)])
