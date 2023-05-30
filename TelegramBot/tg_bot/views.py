from tg_bot import app
from flask import request
from .handlers import TelegramHandler
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
TG_BASE_URL = os.getenv("TG_BASE_URL")

@app.route('/', methods=["POST"])
def hello():
    handler = TelegramHandler(request.json)
    handler.handle()
    return 'ok'



