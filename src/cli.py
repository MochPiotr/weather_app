from utils import format_weather_data, get_weather

API_KEY = open('key/api_key', 'r').read().strip()

if __name__ == "__main__":
    city_name = input("Choose city to check weather: ").strip()
    if not city_name:
        print("No city input!")
        exit()

    print(f"DEBUG: Checking weather for '{city_name}'")

    data = get_weather(city_name, API_KEY)
    formatted = format_weather_data(data, city_name)

    print(f"Temperature in {city_name}: {formatted['Temperature_c']:.2f}°C or {formatted['Temperature_f']:.2f}°F")
    print(f"Feels like: {formatted['Feels_like_c']:.2f}°C or {formatted['Feels_like_f']:.2f}°F")
    print(f"Humidity: {formatted['Humidity']}%")
    print(f"Description: {formatted['Description']}")
    print(f"Sunrise: {formatted['Sunrise']}")
    print(f"Sunset: {formatted['Sunset']}")
