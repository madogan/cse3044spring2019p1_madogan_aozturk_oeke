from app import app
from os.path import join
from app.forms import LoginForm
from flask import render_template, request, flash, redirect


@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main/index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            flash('Login requested for user {}, remember_me={}'.format(form.email.data, form.remember_me.data))
            return redirect('/')
    return render_template('auth/login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    print(request.form)
    return render_template('auth/register.html')

@app.errorhandler(404)
def error(e):
    """
        TODO:
            * Repeat this for other error types.
                (http://flask.pocoo.org/docs/1.0/patterns/errorpages/)
    """
    return render_template('error/error.html', error={'code': 404, 'message': "Not Found!"})