from flask import Flask
from logging.config import dictConfig
from .config import AppConfig

app = Flask(__name__)
app.secret_key = 'secret_key'

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }}

})

app.config.from_object(AppConfig)

from .views import *
from .class_based_views import *