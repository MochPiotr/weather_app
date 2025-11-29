from src.main import kelvin_to_celsius_fahrenheit

def test_kelvin_to_celsius_fahrenheit():
    celsius, fahrenheit = kelvin_to_celsius_fahrenheit(273.15)
    assert round(celsius, 2) == 0
    assert round(fahrenheit, 2) == 32