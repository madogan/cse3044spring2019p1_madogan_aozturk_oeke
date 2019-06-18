from uuid import uuid4

from app import db
from app import app
from app.models import *
from os.path import join
from app.forms import LoginForm, RegisterForm, QuestionForm
from flask_login import current_user, login_user, logout_user, login_required
from flask import render_template, request, flash, redirect, url_for, g


@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main/index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash("Halihazırda bir kullanıcı giriş yapmış bulunmaktadır.")
        return redirect(url_for('login'))

    register_form = RegisterForm()
    if request.method == "POST":
        if register_form.validate_on_submit():
            new_user = User(
                first_name = register_form.first_name.data,
                last_name = register_form.last_name.data,
                email = register_form.email.data,
                uuid = uuid4()
            )

            new_user.set_password(register_form.password.data)

            new_user.set_username()

            old_user = db.session.query(User).filter(User.email==new_user.email).first()

            if old_user is None:
                db.session.add(new_user)
                db.session.commit()
                flash("Başarılı bir şekilde kayıt tamamlandı. Giriş yapabilirsiniz...", "success")
                return redirect('login')
            else:  # user exist
                flash("Bu kullanıcı mevcut.", "warning")
                return redirect('register')
        else:
            return render_template("auth/register.html", title="Kayıt", form=register_form)
    if request.method == "GET":
        return render_template("auth/register.html", title="Kayıt", form=register_form)
    return render_template('error/error.html', error={'code': 400, 'message': "Bad Request!"})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash("Halihazırda giriş yapmış bulunmaktasınız.")
        return redirect(url_for('index'))
    
    login_form = LoginForm()
    if request.method == "POST":
        if login_form.validate_on_submit():
            user = User.query.filter_by(email=login_form.email.data).first()
            if user is None or not user.check_password(login_form.password.data):
                flash('Geçersiz eposta veya parola.')
                return redirect(url_for('login'))
            login_user(user)
            return redirect(url_for('index'))
    return render_template('auth/login.html', form=login_form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user/<username>', methods=["POST", "GET"])
def user(username):
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    
    question_form = QuestionForm()
    if request.method == "POST":
        if question_form.validate_on_submit():
            question = Question(
                asker_id=current_user.id,
                asker_name=current_user.first_name + " " + current_user.last_name,
                topic=question_form.topic.data,
                content=question_form.question.data,
                category=question_form.category.data
            )
            
            db.session.add(question)
            db.session.commit()

            return redirect(url_for('q_a'))
        else:
            flash("Dikkatli ol biraz :)")
            return render_template('user/main.html', form=question_form)
    if request.method == "GET":
        return render_template('user/main.html', form=question_form)


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('main/about.html')


@app.route('/q_a', methods=['GET', 'POST'])
def q_a():
    questions = Question.query.all()
    return render_template('main/q_a.html', questions=questions)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('main/contact.html')


@app.route('/experts', methods=['GET', 'POST'])
def experts():
    return render_template('main/experts.html')


@app.route('/categor/<category>', methods=['GET', 'POST'])
def category(category):
    return render_template(f'main/{category}.html')    


@app.route('/question/<qid>', methods=['GET', 'POST'])
def question(qid):
    question = Question.query.get(qid)
    question.date = question.date.strftime("%c")
    return render_template(f'main/question.html', question=question)    


@app.errorhandler(404)
def error(e):
    """
        TODO:
            * Repeat this for other error types.
                (http://flask.pocoo.org/docs/1.0/patterns/errorpages/)
    """
    return render_template('error/error.html', error={'code': 404, 'message': "Not Found!"})
