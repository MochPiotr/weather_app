from fastapi import APIRouter, HTTPException
from utils import get_weather, format_weather_data
from models.weather_models import WeatherResponse
from config.settings import API_KEY

router = APIRouter(prefix="/weather")

@router.get("/{city}", response_model=WeatherResponse)
def weather(city: str) -> WeatherResponse:
    clean_city = city.replace("-", "").replace(" ", "").strip()

    if not clean_city.isalpha():
        raise HTTPException(status_code=400, detail="City must contain only letters")

    try:
        data = get_weather(city, API_KEY)
    except ValueError as e:
        if str(e) == "CITY_NOT_FOUND":
            raise HTTPException(404, "City not found")
        elif str(e) == "INVALID_API_KEY":
            raise HTTPException(401, "Invalid API key")
        else:
            raise HTTPException(500, "Weather service unavailable")

    formatted = format_weather_data(data, city)
    return formatted
