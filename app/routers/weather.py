from fastapi import APIRouter, HTTPException
from utils import get_weather, format_weather_data
from models.weather_models import WeatherResponse
from config.settings import API_KEY

router = APIRouter(
    prefix="/weather",
    tags=["Weather"]
)

@router.get("/{city}", response_model=WeatherResponse)
def weather(city: str):
    clean_city = city.replace("-", "").replace(" ", "").strip()

    if not clean_city.isalpha():
        raise HTTPException(status_code=400, detail="City must contain only letters")

    try:
        data = get_weather(city, API_KEY)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    formatted = format_weather_data(data, city)
    return formatted
