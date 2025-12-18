from fastapi import FastAPI
from routers.weather import router as weather_router
from fastapi import status


app = FastAPI(
    title="Weather API",
    description="Simple FastAPI app using OpenWeather API",
    version="1.0.0",
)

app.include_router(weather_router)


@app.get("/health", status_code=status.HTTP_200_OK)
def health():
    return {"status": "ok"}