import requests
from tg_bot import app
from flask import request

BOT_TOKEN = '5901762373:AAF5YvUzGor139zpNHZnWfQSBww38cQL_p8'
TG_BASE_URL = 'https://api.telegram.org/bot'

@app.route('/', methods=["POST"])
def hello():
    message = request.json.get('message')
    chat_id = message.get('chat').get('id')
    user_name = message.get('from').get('first_name')
    text = f'Hello, {user_name}!'
    data = {
        'chat_id': chat_id,
        'text': text
    }
    requests.post(f'{TG_BASE_URL}{BOT_TOKEN}/sendMessage', json=data)
    return 'ok'
