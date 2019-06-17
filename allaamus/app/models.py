import datetime

from app import db, login_manager
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, index=True, primary_key=True)
    uuid = db.Column(UUID(as_uuid=True), index=True, unique=True, nullable=False)
    email = db.Column(db.String(256), index=True, unique=True)
    first_name = db.Column(db.String(24), nullable=False)
    last_name = db.Column(db.String(24), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    register_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow(), nullable=False)

    questions = relationship("Question")
    answers = relationship("Answer")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User({self.id}): {self.first_name} {self.last_name}>'


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, index=True, primary_key=True)
    source = db.Column(db.String(), nullable=False)
    url = db.Column(db.String(), nullable=False)
    category = db.Column(db.String(), nullable=False)
    date = db.Column(db.DateTime(), nullable=False)
    title = db.Column(db.String(), nullable=False)
    content = db.Column(db.String(), nullable=False)
    tags = db.Column(db.String(), nullable=True)

    def __repr__(self):
        return f'<Article({self.id}): {self.title}>'


class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, index=True, primary_key=True)
    asker_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    content = db.Column(db.String(), nullable=False)
    date = db.Column(db.DateTime(), nullable=False)
    category = db.Column(db.String(), nullable=False)
    
    answers = relationship("Answer")

class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, index=True, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    answerer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    content = db.Column(db.String(), nullable=False)
    date = db.Column(db.DateTime(), nullable=False)
