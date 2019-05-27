from app import app
from flask import render_template, request, flash, redirect
from app.forms import LoginForm


@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.email.data, form.remember_me.data))
        return redirect('/')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@app.errorhandler(404)
def error(e):
    """
        TODO:
            * Repeat this for other error types.
                (http://flask.pocoo.org/docs/1.0/patterns/errorpages/)
    """
    return render_template('error.html', error={'code': 404, 'message': "Not Found!"})