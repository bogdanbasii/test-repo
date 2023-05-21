import requests
from tg_bot import app
from flask import request
from .handlers import TelegramHandler

BOT_TOKEN = '5901762373:AAF5YvUzGor139zpNHZnWfQSBww38cQL_p8'
TG_BASE_URL = 'https://api.telegram.org/bot'

@app.route('/', methods=["POST"])
def hello():
    handler = TelegramHandler(request.json)
    handler.handle()
    return 'ok'



