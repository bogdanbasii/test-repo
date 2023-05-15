import requests

BOT_TOKEN = '5901762373:AAF5YvUzGor139zpNHZnWfQSBww38cQL_p8' # TODO move to env
TG_BASE_URL = 'https://api.telegram.org/bot'

class TelegramHandler:


# class Horoscope:
# #     def __init__(self, first_name, id, is_bot, language_code, username):
# #         self.first_name = first_name
# #         self.id = id
# #         self.is_bot = is_bot
# #         self.language_code = language_code
# #         self.username = username
# # class TelegramHandler:
# #     user = None
# #     def __init__(self, data):
# #         self.user = User(**data.get('message').get('from'))
# #         print(self.user)
# #         print(self.user.id)
# #
# #     def send_message(self, text):
# #         data = {
# #             'chat_id': self.user.id,
# #             'text': text
# #         }
# #         requests.post(f'{TG_BASE_URL}{BOT_TOKEN}/sendMessage', json=data)
#     def get_horoscope(sign):
#         url = f"https://horoscopes-ai.p.rapidapi.com/get_horoscope/{sign}/today/general/en"
#         headers = {
#             "X-RapidAPI-Key": "898136ea7emsh51f1d621b4ff98ep1326e3jsna30eedea91c6",
#             "X-RapidAPI-Host": "horoscopes-ai.p.rapidapi.com"
#         }
#         response = requests.get(url, headers=headers)
#         return response.json()['horoscope']
#
#
#     def horoscope(update, context):
#         message = update.message.text.split(' ')
#         if len(message) == 2:
#             sign = message[1]
#             horoscope_text = get_horoscope(sign)
#             update
