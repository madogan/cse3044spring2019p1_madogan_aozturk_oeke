import re
from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Email, AnyOf, Length, EqualTo, Regexp


class RegisterForm(FlaskForm):
    first_name = StringField('Ad', [
        DataRequired(message="Bu alan boş bırakılamaz."),
        Length(min=2, max=24, message="Bu alan en az 2 en fazla 24 harf içerebilir."),
        Regexp(r'^[a-zA-ZğüşöçĞÜİŞıÇÖ]+$', re.I | re.U, message="Geçersiz karakter içeriyor.")
    ])
    last_name = StringField('Soyad', [
        DataRequired(message="Bu alan boş bırakılamaz."),
        Length(min=2, max=24, message="Bu alan en az 2 en fazla 24 harf içerebilir."),
        Regexp(r'^[a-zA-ZğüşöçĞÜİŞıÇÖ]+$', re.I | re.U, message="Geçersiz karakter içeriyor.")
    ])
    email = StringField('Eposta', [
        DataRequired(message="Bu alan boş bırakılamaz."),
        Email(message="Email biçimi doğru değil: xyz@abc.com şeklinde olmalı.")
    ])
    password = PasswordField('Parola', [
        DataRequired(message="Bu alan boş bırakılamaz."),
        Length(min=6, max=24, message="Bu alan en az 6 en fazla 24 harf içerebilir."),
        Regexp(r'^[a-zA-ZğüşöçĞÜİŞıÇÖ0-9@#$%^&+=]+$', re.I | re.U, message="Geçersiz karakter içeren parola.")
    ])
    confirm_password = PasswordField('Doğrulama Parolası', [
        DataRequired(message="Bu alan boş bırakılamaz."),
        Length(min=6, max=24, message="Bu alan en az 6 en fazla 24 harf içerebilir."),
        EqualTo('password', message="İki parolanın uyuşması gerek."),
        Regexp(r'^[a-zA-ZğüşöçĞÜİŞıÇÖ0-9@#$%^&+=]+$', re.I | re.U, message="Geçersiz karakter içeren parola.")
    ])
    user_type = StringField("Kullanıcı Türü", [
        DataRequired(message="Bu alan boş bırakılamaz."),
        Regexp(r'(meraklı|usta)', re.I | re.U, message="Kullanıcı türü: 'meraklı' yada 'usta' olmalıdır.")
    ])
    submit = SubmitField("Kayıt")

    def pre_process_user_type(self, field):
        pass

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
