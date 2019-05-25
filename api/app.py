from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField


db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://root:admin@localhost:5432/allaamus_db'


class RegistrationForm(Form):
    first_name = StringField('First Name', [
        validators.Length(min=3, max=25),
        validators.DataRequired()
    ])
    last_name = StringField('Last Name', [
        validators.Length(min=3, max=25),
        validators.DataRequired()
    ])
    age = IntegerField('Age', [
        validators.DataRequired(),
        validators.DataRequired()
    ])
    job = StringField('Job', [
        validators.Length(min=4, max=25),
        validators.DataRequired()
    ])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    email = StringField('Email Address', [
        validators.Length(min=6, max=35),
        validators.DataRequired(),
        validators.Email()
    ])
    phone = StringField('Phone Number', [
        validators.Length(min=10, max=16),
        validators.DataRequired()
    ])
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(48), nullable=False)
    last_name = db.Column(db.String(48), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    job = db.Column(db.String, nullable=False)
    email = db.Column(db.String(192), unique=True, nullable=False)
    phone = db.Column(db.String(16), unique=True, nullable=False)
    activation = db.Column(db.Boolean, unique=False, default=False)

    def __repr__(self):
        return f'{self.id}: {self.first_name} {self.last_name} (Activation Status: {self.activation})'




@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST':
        if form.validate():
            new_user = User(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                age=form.age.data,
                job=form.job.data,
                email=form.email.data,
                phone=form.phone.data,
                activation=True
            )
            db.session.add(new_user)
            flash('Thanks for registering')
            return redirect(url_for('/login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['POST'])
def login():
    return 'Login'


