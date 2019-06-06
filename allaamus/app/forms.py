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
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    first_name = StringField('Ad', validators=[
        validators.DataRequired()
    ])
    last_name = StringField('Soyad', validators=[
        validators.DataRequired()
    ])
    email = StringField('Eposta', validators=[
        validators.DataRequired(),
        validators.Email()
    ])
    password = PasswordField('Parola', validators=[
        validators.DataRequired(),
        validators.Length(min=6, max=24)
    ])
    confirm_password = PasswordField('Doğrulama Parolası', validators=[
        validators.DataRequired(),
        validators.Length(min=6, max=24)
    ])
    user_type = StringField("Kullanıcı Türü", validators=[
        validators.DataRequired(),
        validators.AnyOf(["meraklı", "usta"])
    ])
