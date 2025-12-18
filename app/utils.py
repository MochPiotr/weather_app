import datetime as dt
import requests
from typing import Dict, Tuple

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city: str, api_key: str) -> Dict:
    params = {
        "appid": api_key,
        "q": city
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
    except requests.RequestException:
        raise ValueError("WEATHER_API_DOWN")

    if response.status_code == 404:
        raise ValueError("CITY_NOT_FOUND")

    if response.status_code == 401:
        raise ValueError("INVALID_API_KEY")

    if response.status_code != 200:
        raise ValueError("WEATHER_API_ERROR")

    return response.json()

def kelvin_to_celsius_fahrenheit(kelvin: float) -> Tuple[float, float]:
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return round(celsius, 2), round(fahrenheit, 2)

def format_weather_data(data: Dict, city: str) -> Dict:
    temp_kelvin = data["main"]["temp"]
    feels_like_kelvin = data["main"]["feels_like"]

    temp_c, temp_f = kelvin_to_celsius_fahrenheit(temp_kelvin)
    feels_c, feels_f = kelvin_to_celsius_fahrenheit(feels_like_kelvin)

    sunrise = dt.datetime.utcfromtimestamp(
        data["sys"]["sunrise"] + data["timezone"]
    ).isoformat()

    sunset = dt.datetime.utcfromtimestamp(
        data["sys"]["sunset"] + data["timezone"]
    ).isoformat()

    return {
        "city": city,
        "temperature_c": temp_c,
        "temperature_f": temp_f,
        "feels_like_c": feels_c,
        "feels_like_f": feels_f,
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
        "sunrise": sunrise,
        "sunset": sunset,
    }
