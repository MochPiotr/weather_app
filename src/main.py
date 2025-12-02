from fastapi import FastAPI, HTTPException
from utils import get_weather, format_weather_data


API_KEY = open('key/api_key').read().strip()

app = FastAPI()

@app.get("/weather/{city}")
def weather(city: str):
    clean_city = city.replace("-","").replace(" ","")

    if not clean_city.isalpha():
        raise HTTPException(status_code=400, detail="City must contain only letters")
    
    try:
        data = get_weather(city, API_KEY)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


    formatted = format_weather_data(data, city)
    return formatted