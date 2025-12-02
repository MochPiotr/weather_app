import datetime as dt
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

def get_weather(city: str, api_key):
    params = {
        "appid":  api_key,
        "q": city
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 404:
        raise ValueError("City not found")

    if response.status_code != 200:
        raise Exception(f"API returned status {response.status_code}: {response.text}")

    return response.json()

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

def format_weather_data(data, city):
    temp_kelvin = data['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)

    feels_like_kelvin = data['main']['feels_like']
    feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)

    humidity = data['main']['humidity']
    description = data['weather'][0]['description']

    sunrise_time = str(dt.datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone']))
    sunset_time = str(dt.datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone']))


    return {
        "city": city,
        "Temperature_c": temp_celsius,
        "Temperature_f": temp_fahrenheit,
        "Feels_like_c": feels_like_celsius,
        "Feels_like_f": feels_like_fahrenheit,
        "Humidity": humidity,
        "Description": description,
        "Sunrise": sunrise_time,
        "Sunset": sunset_time,
    }
