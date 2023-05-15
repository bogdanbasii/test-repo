import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

BOT_TOKEN = '5901762373:AAF5YvUzGor139zpNHZnWfQSBww38cQL_p8'
TG_BASE_URL = 'https://api.telegram.org/bot'

class User:
    def __init__(self, first_name, id, is_bot, language_code, username):
        self.first_name = first_name
        self.id = id
        self.is_bot = is_bot
        self.language_code = language_code
        self.username = username

class TelegramHandler:
    user = None
    text = None
    data = None

    def __init__(self, data):
        message = data.get('message')
        callback_query = data.get('callback_query')
        if message:
            self.user = User(**message.get('from'))
            self.text = message.get('text')
        elif callback_query:
            self.user = User(**callback_query.get('from'))
            self.data = callback_query.get('data')

    def handle_start(self):
        text = "Hello, welcome to Horoscope Bot! Please choose your horoscope sign."
        buttons = [
            [InlineKeyboardButton("Aries", callback_data='aries')],
            [InlineKeyboardButton("Taurus", callback_data='taurus')],
            [InlineKeyboardButton("Gemini", callback_data='gemini')],
            [InlineKeyboardButton("Cancer", callback_data='cancer')],
            [InlineKeyboardButton("Leo", callback_data='leo')],
            [InlineKeyboardButton("Virgo", callback_data='virgo')],
            [InlineKeyboardButton("Libra", callback_data='libra')],
            [InlineKeyboardButton("Scorpio", callback_data='scorpio')],
            [InlineKeyboardButton("Sagittarius", callback_data='sagittarius')],
            [InlineKeyboardButton("Capricorn", callback_data='capricorn')],
            [InlineKeyboardButton("Aquarius", callback_data='aquarius')],
            [InlineKeyboardButton("Pisces", callback_data='pisces')]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        self.send_markupmessage(text, reply_markup)

    def send_markupmessage(self, text, markup):
        data = {
            'chat_id': self.user.id,
            'text': text,
            'reply_markup': markup
        }
        requests.post(f'{TG_BASE_URL}{BOT_TOKEN}/sendMessage', json=data)

    def handle(self):
        if self.text:
            text = self.text.lower()  # convert message text to lower case
            if text.startswith('/start'):
                self.handle_start()
        elif self.data:  # handle callback data
            horoscope = self.get_horoscope(self.data)
            self.send_message(horoscope)

    def send_message(self, text):
        data = {
            'chat_id': self.user.id,
            'text': text
        }
        requests.post(f'{TG_BASE_URL}{BOT_TOKEN}/sendMessage', json=data)

    def get_horoscope(self, sign):
        url = "https://horoscopeapi-horoscope-v1.p.rapidapi.com/daily"
        querystring = {"date": "today", "sign": sign}
        headers = {
            "X-RapidAPI-Key": "3f43de580cmshd27bd26bd5e0138p1a9edbjsn021a1e5e57b5",
            "X-RapidAPI-Host": "horoscopeapi-horoscope-v1.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            return response.json().get('horoscope')
        else:
            return "Sorry, I couldn't fetch the horoscope for you."