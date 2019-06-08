from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from app.config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)

from app import routes, models
