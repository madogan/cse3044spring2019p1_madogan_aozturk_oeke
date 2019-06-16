import sqlalchemy as db

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import AllaamusScraper.settings

DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    engine = db.create_engine(URL(**settings.DATABASE))
    return engine


def create_deals_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class BilimfiliItem(DeclarativeBase):
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
