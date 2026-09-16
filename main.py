from src.config import GEOCODING_URL,WEATHER_URL,API_KEY
from src.extract import extract
#from src.storage import save_raw
from src.validation import validation
from src.transform import transform
import pandas as pd



extract_data = extract(GEOCODING_URL, WEATHER_URL, API_KEY)

validation_data = validation(extract_data)

transform_data = transform(validation_data)



print(extract_data)
