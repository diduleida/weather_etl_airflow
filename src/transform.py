import pandas as pd

def transform(data):
    df = pd.json_normalize(data)
    df_weather = pd.json_normalize(data, record_path=['weather'], meta=['name'])
    df_weather = df_weather.add_prefix('weather.')
    df = df.merge(df_weather, left_on='name', right_on='weather.name')
    df = df.drop(columns=['weather.name','weather','base','sys.type','sys.id'])
    # unit - які одиниці; utc - інтерпритувати в такому форматі
    df['dt'] = pd.to_datetime(df['dt'], unit='s', utc=True)
    df['sys.sunrise'] = pd.to_datetime(df['sys.sunrise'], unit='s', utc=True)
    df['sys.sunset'] = pd.to_datetime(df['sys.sunset'], unit='s', utc=True)
    df = df.rename(columns={
        'coord.lon':'longitude',
        'coord.lat':'latitude',
        'main.temp':'temperature',
        'main.feels_like':'feels_like',
        'main.temp_min':'temp_min',
        'main.temp_max':'temp_max',
        'main.pressure':'pressure',
        'main.humidity':'humidity',
        'main.sea_level':'sea_level',
        'main.grnd_level':'ground_level',
        'wind.speed':'wind_speed',
        'wind.deg':'wind_deg',
        'wind.gust':'wind_gust',
        'clouds.all':'cloudness',
        'sys.country':'country',
        'sys.sunrise':'sunrise',
        'sys.sunset':'sunset',
        'rain.1h':'rain_1h',
        'dt':'datatime',
        'weather.id':'weather_id',
        'weather.main':'weather_main',
        'weather.description':'weather_description',
        'weather.icon':'weather_icon'
    })
    return df