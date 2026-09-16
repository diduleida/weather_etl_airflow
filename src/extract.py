import requests
from .config import cities




def extract(GEOCODING_URL, WEATHER_URL, API_KEY):
    data_final = []
    for city, country in cities:
        parametrs = {
            'q': f'{city},{country}',
            'limit': 5,
            'appid': API_KEY
        }
        response = requests.get(GEOCODING_URL,params=parametrs).json()

        city_result = next(
            (
            item for item in response
            if item.get('local_names', {}).get('en','').lower() == city.lower()
            or item.get('name', '').lower() == city.lower()
            ),
            None
        )

        if  city_result is None:
            raise ValueError(f'Could not find exact city: {city}, {country}')

        lat = city_result['lat'] 
        lon = city_result['lon']

        url = f'{WEATHER_URL}?lat={lat}&lon={lon}&appid={API_KEY}'

        data = requests.get(url).json()

        data['name'] = city

        data_final.append(data)

    return data_final

 