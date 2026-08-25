import requests
from .config import cities




def extract(GEOCODING_URL, WEATHER_URL, API_KEY):
    data_final = []
    for city, country in cities:
        parametrs = {
            'q': f'{city},{country}',
            'limit': 1,
            'appid': API_KEY
        }
        response = requests.get(GEOCODING_URL,params=parametrs).json()
        lat = response[0]['lat'] 
        lon = response[0]['lon']

        url = f'{WEATHER_URL}?lat={lat}&lon={lon}&appid={API_KEY}'
        data = requests.get(url).json()
        data_final.append(data)
    return data_final

 