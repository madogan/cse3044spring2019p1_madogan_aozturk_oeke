from app import app
from os.path import join
from app.forms import LoginForm, RegisterForm
from flask import render_template, request, flash, redirect
from app.models import *
from app import db
from werkzeug.security import generate_password_hash

@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main/index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if request.method == "POST":
        if register_form.validate_on_submit():
            new_user = User(
                first_name = register_form.first_name.data,
                last_name = register_form.last_name.data,
                email = register_form.email.data,
                password_hash = generate_password_hash(register_form.password.data),
                user_type = register_form.user_type.data
            )

            old_user = db.session.query(User).filter(User.email==new_user.email).first()

            if old_user is None:
                db.session.add(new_user)
                db.session.commit()
                return redirect('login')
            else:  # user exist
                return render_template('error/error.html', error={'code': 31, 'message': "User exist"})
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


@app.route('/page-about', methods=['GET', 'POST'])
def page_about():
    return render_template('main/page-about.html')
    
@app.route('/blog', methods=['GET', 'POST'])
def blog():
    return render_template('main/blog.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('main/page-contact.html')

@app.route('/experts', methods=['GET', 'POST'])
def experts():
    return render_template('main/page-services.html')

@app.errorhandler(404)
def error(e):
    """
        TODO:
            * Repeat this for other error types.
                (http://flask.pocoo.org/docs/1.0/patterns/errorpages/)
    """
    return render_template('error/error.html', error={'code': 404, 'message': "Not Found!"})