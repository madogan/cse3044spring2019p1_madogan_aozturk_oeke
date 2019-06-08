import os

class BaseConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'bilemezsin_kiii'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgres://madogan:admin@localhost:5432/allaamus_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
