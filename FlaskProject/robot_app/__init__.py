import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from logging.config import dictConfig
from .config import AppConfig

db = SQLAlchemy()
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }}

})

app.config.from_object(AppConfig)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

db.init_app(app)

from .views import *
from .class_based_views import *
from .models import *

with app.app_context():
    db.create_all()