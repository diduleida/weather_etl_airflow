import pandas as pd



def validation(data):
    # розготртаємо вкладені списки
    df = pd.json_normalize(data)
    if df['id'].isna().any():
        raise ValueError("Missing id")
    if df.empty:
        raise ValueError("DataFrame is empty")
    if df['id'].duplicated().any():
        raise ValueError("Dublicated id")
    if df['coord.lon'].isna().any():
        raise ValueError("lon")
    if df['coord.lat'].isna().any():
        raise ValueError("Missing lat")
    if df['name'].isna().any():
        raise ValueError("Missing name")
    # проходимось по кожному елементу x і якщо хоч один пустий то raise
    if df['weather'].apply(lambda x: not x).any():
        raise ValueError("Missing weather-data")
    return data




 