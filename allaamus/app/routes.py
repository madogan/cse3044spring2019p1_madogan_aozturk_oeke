from app import app
from os.path import join
from app.forms import LoginForm, RegisterForm
from flask import render_template, request, flash, redirect
from app.models import *
from app import db

@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main/index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
        TODO:
            * Hata mesajı döndürme mekanizması eklenecek.
    """
    register_form = RegisterForm()
    if request.method == "POST":
        if register_form.validate_on_submit():
            new_user = User(
                first_name = register_form.first_name.data,
                last_name = register_form.last_name.data,
                email = register_form.email.data,
                password_hash = register_form.password.data,
                user_type = register_form.user_type.data
            )
            if User.query.get(new_user) is not None:
                
                db.session.add(new_user)
                db.session.commit()
            else:  # user exist
                render_template('error/error.html', error={'code': 31, 'message': "User exist"})
            return redirect('login')
        else:
            return render_template("auth/register.html", title="Kayıt", form=register_form)
    if request.method == "GET":
        return render_template("auth/register.html", title="Kayıt", form=register_form)
    return render_template('error/error.html', error={'code': 404, 'message': "Not Found!"})

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            flash('Login requested for user {}, remember_me={}'.format(form.email.data, form.remember_me.data))
            return redirect('/')
    return render_template('auth/login.html', form=form)


@app.errorhandler(404)
def error(e):
    """
        TODO:
            * Repeat this for other error types.
                (http://flask.pocoo.org/docs/1.0/patterns/errorpages/)
    """
    return render_template('error/error.html', error={'code': 404, 'message': "Not Found!"})