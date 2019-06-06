
from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Email, AnyOf, Length


class RegisterForm(FlaskForm):
    first_name = StringField('Ad', [
        InputRequired()
    ])
    last_name = StringField('Soyad', [
        InputRequired()
    ])
    email = StringField('Eposta', [
        InputRequired(),
        Email()
    ])
    password = PasswordField('Parola', [
        InputRequired(),
        Length(min=6, max=24)
    ])
    confirm_password = PasswordField('Doğrulama Parolası', [
        InputRequired(),
        Length(min=6, max=24)
    ])
    user_type = StringField("Kullanıcı Türü", [
        InputRequired(),
        AnyOf(["meraklı", "usta"])
    ])
    submit = SubmitField("Kayıt")

class LoginForm(FlaskForm):
    email = StringField('Eposta', [
        InputRequired(),
        Email()
    ])
    password = PasswordField('Parola', [
        InputRequired(),
        Length(min=6, max=24)
    ])
    submit = SubmitField('Giriş')


