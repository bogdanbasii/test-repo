class Bot:
    def __init__(self, name):
        self.name = name

    def send_message(self, message):
        print(message)

    def say_name(self):
        print(self.name)

some_bot = Bot("Peter")
some_bot.say_name()
some_bot.send_message("Hello")


class TelegramBot(Bot):
    def __init__(self, name):
        super().__init__(name)
        self.url = None
        self.chat_id = None
        
    def send_message(self, message):
        print(f"{self.name} bot says {message} to chat {self.chat_id} using {self.url}")

    def set_url(self, url):
        self.url = url
    def set_chat_id(self, chat_id):
        self.chat_id = chat_id

telegram_bot = TelegramBot("TG")
telegram_bot.say_name()
telegram_bot.send_message("Hello")
telegram_bot.set_chat_id(None)
telegram_bot.set_url(None)

