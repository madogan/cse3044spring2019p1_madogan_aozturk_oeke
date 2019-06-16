import AllaamusScraper.settings as settings

from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Enum


DeclarativeBase = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    engine = create_engine(URL(**settings.DATABASE))
    return engine


def create_bilimfili_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class BilimfiliItem(DeclarativeBase):
    __tablename__ = 'article'
    id = Column(Integer, index=True, primary_key=True)
    source = Column(String(), nullable=False)
    url = Column(String(), nullable=False)
    category = Column(String(), nullable=False)
    date = Column(DateTime(), nullable=False)
    title = Column(String(), nullable=False)
    content = Column(String(), nullable=False)
    tags = Column(String(), nullable=True)

    def __repr__(self):
        return f'<Article({self.id}): {self.title}>'
