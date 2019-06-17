import datetime

from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, index=True, primary_key=True)
    email = db.Column(db.String(256), index=True, unique=True)
    first_name = db.Column(db.String(24), nullable=False)
    last_name = db.Column(db.String(24), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    user_type = db.Column(db.Enum('meraklı', 'usta', name='user_types'))
    register_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow(), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User({self.id}): {self.first_name} {self.last_name}>'


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))