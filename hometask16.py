import json
import requests
import random

sites = ["https://google.com", "https://facebook.com", "https://twitter.com", "https://amazon.com", "https://apple.com"]
random_site = random.choice(sites)
response = requests.get(random_site)
print("Site: ", random_site)
print("Status code: ", response.status_code)
print("HTML length: ", len(response.text))

import json

city = input("Enter city name: ")
url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
response = requests.get(url)
data = json.loads(response.text)
res = data.get('results')
coordinates = res[0]['latitude'], res[0]['longitude']
url = f"https://api.open-meteo.com/v1/forecast?latitude={coordinates[0]}&longitude={coordinates[1]}&current_weather=true"
response = requests.get(url)
data = response.json()
current_weather = data["current_weather"]
for i in current_weather:
    print(i, current_weather[i])

