from app.utils import kelvin_to_celsius_fahrenheit, get_weather, format_weather_data
from unittest.mock import patch
import pytest

def test_kelvin_to_celsius_fahrenheit():
    celsius, fahrenheit = kelvin_to_celsius_fahrenheit(273.15)
    assert celsius == 0
    assert fahrenheit == 32

def test_format_weather_data():
    sample_data = {
        "main": {"temp": 300, "feels_like": 298, "humidity": 50},
        "weather": [{"description": "clear sky"}],
        "sys": {"sunrise": 1700000000, "sunset": 1700005000},
        "timezone": 0
    }
    result = format_weather_data(sample_data, "London")
    assert result["city"] == "London"
    assert "temperature_c" in result

def test_get_weather_ok():
    with patch("app.utils.requests.get") as mock:
        mock.return_value.status_code = 200
        mock.return_value.json.return_value = {"main": {"temp": 280}, "weather": [{"description": "clear"}], "sys": {"sunrise":0,"sunset":0}, "timezone":0}

        res = get_weather("London", "KEY")
        assert res["main"]["temp"] == 280

def test_get_weather_404():
    with patch("app.utils.requests.get") as mock:
        mock.return_value.status_code = 404

        with pytest.raises(ValueError):
            get_weather("UnknownCity", "KEY")

def test_get_weather_500():
    with patch("app.utils.requests.get") as mock:
        mock.return_value.status_code = 500
        mock.return_value.text = "Server Error"

        with pytest.raises(ValueError):
            get_weather("London", "KEY")
