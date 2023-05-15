import requests
HOROSCOPE_URL: "https://horoscopes-ai.p.rapidapi.com/get_horoscope_en/%7Bsign%7D/%7Bperiod%7D/general"

class HoroscopeServiceException(Exception):
    pass
HOROSCOPE_URL: "https://horoscopes-ai.p.rapidapi.com/get_horoscope_en/{sign}/{period}/general"

class HoroscopeService:
    @staticmethod
    def get_sign(sign):
        url = HOROSCOPE_URL.format(sign=sign, period='today')
        headers = {
            "X-RapidAPI-Key": "898136ea7emsh51f1d621b4ff98ep1326e3jsna30eedea91c6",
            "X-RapidAPI-Host": "horoscopes-ai.p.rapidapi.com"
        }
        res = requests.get(url, headers=headers)
        if res.status_code != 200:
            raise HoroscopeServiceException("Cannot get horoscope data")
        return res.json().get('results')


    @staticmethod
    def get_forecast(forecast):
        pass