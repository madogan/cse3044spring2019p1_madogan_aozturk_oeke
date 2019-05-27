from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import validators


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        validators.DataRequired(),
        validators.Email()
    ])
    password = PasswordField('Password', validators=[
        validators.DataRequired(),
        validators.Length(min=6, max=24)
    ])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
  