from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, InputRequired


class Validation(FlaskForm):
    name = StringField("name", validators=[DataRequired(), Length(min=1, max=500)])


class LoginForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Length(min=4, max=500)])
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=100)])
    submit = SubmitField("Login")


class RegisterForm(FlaskForm):
    name = StringField(validators=[InputRequired(), Length(min=4, max=500)])
    email = StringField(validators=[InputRequired(), Length(min=4, max=500)])
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=100)])
    submit = SubmitField("Register")
