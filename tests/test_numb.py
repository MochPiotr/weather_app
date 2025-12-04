from app.utils import kelvin_to_celsius_fahrenheit
from unittest.mock import patch
import pytest
from app.utils import get_weather, format_weather_data

def test_kelvin_to_celsius_fahrenheit():
    celsius, fahrenheit = kelvin_to_celsius_fahrenheit(273.15)
    assert round(celsius, 2) == 0
    assert round(fahrenheit, 2) == 32

def format_weather_data():
    sample_data = {
    "main": {
        "temp": 300,
        "feels_like": 298,
        "humidity": 50,
    },
    "weather": [
        {"description": "clear sky"}
    ],
    "sys": {
        "sunrise": 1700000000,
        "sunset": 1700005000
    },
    "timezone": 0
}
    result = format_weather_data(sample_data, "London")

    assert result["city"] == "London"
    assert "temperature_c" in result

def test_get_weather_ok():
    with patch("src.utils.requests.get") as mock:
        mock.return_value.status_code = 200
        mock.return_value.json.return_value = {"main": {"temp": 280}}

        res = get_weather("London", "KEY")
        assert res["main"]["temp"] == 280

def test_get_weather_404():
    with patch("src.utils.requests.get") as mock:
        mock.return_value.status_code = 404

        with pytest.raises(ValueError):
            get_weather("UnkownCity", "KEY")

def test_get_weather_500():
    with patch("src.utils.requests.get") as mock:
        mock.return_value.status_code = 500
        mock.return_value.text = "Server Error"

        with pytest.raises(Exception):
            get_weather("London", "KEY")
