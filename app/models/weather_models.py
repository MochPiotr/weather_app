from pydantic import BaseModel

class WeatherResponse(BaseModel):
        city: str
        temperature_c: float
        temperature_f: float
        feels_like_c: float
        feels_like_f: float
        humidity: int
        description: str
        sunrise: str
        sunset: str