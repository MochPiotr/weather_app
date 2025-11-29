import datetime as dt
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key', 'r').read().strip()

def city():
    city_name = input("Choose city to check weather: ").strip()
    if not city_name:
        print("No city input!")
        exit()
    return city_name


CITY = city()

print(f"DEBUG: Checking weather for '{CITY}'")

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = kelvin * (9/5) + 32
    return celsius, fahrenheit

def get_weather(city: str):
    params = {
        "appid": API_KEY,
        "q": city
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        raise Exception(f"API returned status {response.status_code}: {response.text}")

    return response.json()

def print_weather_data(data, city):
 
 
    temp_kelvin = data['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)

    feels_like_kelvin = data['main']['feels_like']
    feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)

    humidity = data['main']['humidity']

    description = data['weather'][0]['description']

    sunrise_time = dt.datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone'])


    print(f"Temperature in {CITY}: {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F")
    print(f"Temperature in {CITY} feels like: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F")
    print(f"Humidity in {CITY}: {humidity}%")
    print(f"The weather in {CITY}: {description}")
    print(f"The sunrise in {CITY}: {sunrise_time}")
    print(f"The sunset in {CITY}: {sunset_time}")


if __name__ == "__main__":
    weather_data = get_weather(CITY)
    print_weather_data(weather_data, CITY)