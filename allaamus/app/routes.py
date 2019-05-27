from app import app
from flask import render_template


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Anasayfa - Allaamus', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    return 'Register'
