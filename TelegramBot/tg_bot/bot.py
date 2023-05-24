from telegram import Bot
from dotenv import load_dotenv
import os

load_dotenv()
bot_token = os.getenv('BOT_TOKEN')
bot = Bot(token=bot_token)
