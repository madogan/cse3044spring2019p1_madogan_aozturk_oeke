from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://root:admin@localhost:5432/allaamus_db'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(48), nullable=False)
    last_name = db.Column(db.String(48), nullable=False)
    email = db.Column(db.String(192), unique=True, nullable=False)
    phone = db.Column(db.String(10), unique=True, nullable=False)

    def __repr__(self):
        return f'{self.id}: {self.first_name} {self.last_name}'


@app.route('/login', method=['POST'])
def login():
    return 'Login'


@app.route('/register', method=['POST'])
def register():
    return 'Register'
