from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://root:admin@localhost:5432/allaamus_db'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(48), nullable=False)
    last_name = db.Column(db.String(48), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    job = db.Column(db.String, nullable=False)
    email = db.Column(db.String(192), unique=True, nullable=False)
    phone = db.Column(db.String(10), unique=True, nullable=False)
    activation = db.Column(db.Boolean, unique=False, default=False)

    def __repr__(self):
        return f'{self.id}: {self.first_name} {self.last_name} (Activation Status: {self.activation})'


@app.route('/login', method=['POST'])
def login():
    if request.method == 'POST':
        if __name__ == '__main__':
            email = request.json.get("email", None)
            password = request.json.get("password", None)

            if email is None:
                return

    return 'Login'


@app.route('/register', method=['POST'])
def register():
    return 'Register'
