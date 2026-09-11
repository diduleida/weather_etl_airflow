import os
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv('API_KEY')

GEOCODING_URL = "https://api.openweathermap.org/geo/1.0/direct"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

MINIO_ENDPOINT=os.getenv('MINIO_ENDPOINT')
MINIO_ROOT_USER=os.getenv('MINIO_ROOT_USER')
MINIO_ROOT_PASSWORD=os.getenv('MINIO_ROOT_PASSWORD')
MINIO_BUCKET=os.getenv('MINIO_BUCKET')
MINIO_ACCESS_KEY=os.getenv('MINIO_ACCESS_KEY')
MINIO_SECRET_KEY=os.getenv('MINIO_SECRET_KEY')

cities = [
    ("Kyiv", "UA"),
    ("Sitges", "ES"),
    ("Odesa", "UA"),
    ("Paris", "FR"),
    ("Porto", "PT"),
    ("Kemer", "TR"),
    ("Casablanca", "MA"),
    ("Cape Town", "ZA"),
    ("Tashkent", "UZ"),
    ("Sydney", "AU"),
    ("Dunedin", "NZ"),
    ("Antalaha", "MG"),
    ("San Diego", "US"),
]


DB_USER=os.getenv('DB_USER')
DB_PASSWORD=os.getenv('DB_PASSWORD')
DB_HOST=os.getenv('DB_HOST')
DB_PORT=os.getenv('DB_PORT')
DB_NAME=os.getenv('DB_NAME')

TABLE_NAME=os.getenv('TABLE_NAME')

POSTGRES_USER=os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD=os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB=os.getenv('POSTGRES_DB')
POSTGRES_PORT=os.getenv('POSTGRES_PORT')

FERNET_KEY=os.getenv('FERNET_KEY')

AIRFLOW_UID=os.getenv('AIRFLOW_UID')

AIRFLOW_USER=os.getenv('AIRFLOW_USER')
AIRFLOW_DB_PASSWORD=os.getenv('AIRFLOW_DB_PASSWORD')
AIRFLOW_DB_NAME=os.getenv('AIRFLOW_DB_NAME')
AIRFLOW_DB_PORT=os.getenv('AIRFLOW_DB_PORT')