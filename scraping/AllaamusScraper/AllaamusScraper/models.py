from sqlalchemy import *
from sqlalchemy.engine.url import URL

import settings

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))


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