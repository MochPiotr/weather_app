from fastapi import FastAPI
from utils import get_weather, format_weather_data


API_KEY = open('key/api_key').read().strip()

app = FastAPI()

@app.get("/weather/{city}")
def weather(city: str):
    data = get_weather(city, API_KEY)
    formatted = format_weather_data(data, city)
    return formatted