from flask import Flask
import logging
from logging.config import dictConfig
app = Flask(__name__)

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


@app.route('/hello')
def hello_world():
    app.logger.info("This is a request to '/hello")
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)