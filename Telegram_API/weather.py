#!usr/bin/env python3

import requests
import json

with open('./API.json') as file:
    data = json.load(file)

WEATHER_API = data['weather_API']
WEATHER_URL = f'https://api.openweathermap.org/data/2.5/weather?q=Namur&appid={WEATHER_API}'
TELEGRAM_API = data['telegram_API']
CHANNEL_ID = data['channel_id']
TELEGRAM_URL = f'https://api.telegram.org/bot{TELEGRAM_API}/sendMessage'

if __name__ == '__main__' :
    weather = requests.get(WEATHER_URL).json()
    forecast = weather['weather'][0]['description']
    print(forecast)
    if 'rain' in forecast:
        requests.get(TELEGRAM_URL, params={
            'chat_id': CHANNEL_ID, 
            'text': "It's going to rain today.. Hagrid.."
            })
