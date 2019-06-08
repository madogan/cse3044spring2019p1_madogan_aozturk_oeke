import datetime

from app import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, index=True, primary_key=True)
    email = db.Column(db.String(256), index=True, unique=True)
    first_name = db.Column(db.String(24), nullable=False)
    last_name = db.Column(db.String(24), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    user_type = db.Column(db.Enum('meraklı', 'usta', name='user_types'))
    register_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow(), nullable=False)

    def __repr__(self):
        return f'<User({self.id}): {self.first_name} {self.last_name}>'

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, index=True, primary_key=True)
    source = db.Column(db.String(), nullable=False)
    url = db.Column(db.String(), nullable=False)
    category = db.Column(db.Enum("eğitim", "teknoloji", "psikoloji", name='article_categories'), nullable=False)
    date = db.Column(db.DateTime(), nullable=False)
    title = db.Column(db.String(), nullable=False)
    content = db.Column(db.String(), nullable=False)
    tags = db.Column(db.String(), nullable=True)

    def __repr__(self):
        return f'<Article({self.id}): {self.title}>'
