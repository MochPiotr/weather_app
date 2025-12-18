# Weather App

**Weather Application** built with **FastAPI**. This project demonstrates REST API development, data validation, error handling, testing with Pytest, and Docker deployment. Frontend in React can be added as an enhancement.

---

## Features

* Fetch current weather for a given city using OpenWeather API.
* Validate user input (city name must contain only letters).
* Handle API errors gracefully:

  * 404 – City not found
  * 401 – Invalid API key
  * 500 – Server errors
* Return well-structured JSON responses.
* Unit tested with Pytest.
* Dockerized for easy deployment.
* Optional: Connect a React frontend to fetch and display data.

---

## Project Structure

```
weather-app/
├── app/
│   ├── main.py             # FastAPI entrypoint
│   ├── utils.py            # Helper functions: API requests, formatting
│   ├── models/
│   │   └── weather_models.py   # Pydantic models for API responses
│   ├── routers/
│   │   └── weather.py      # FastAPI router with endpoints
├── tests/
│   ├── test_utils.py       # Unit tests for utils functions
│   └── test_weather.py     # Optional tests for routers
├── Dockerfile
├── requirements.txt
├── README.md
```

---

## API Usage

### Endpoint

```
GET /weather/{city}
```

### Example Request

```
GET /weather/London
```

### Example Response

```json
{
  "city": "London",
  "temperature_c": 20.5,
  "temperature_f": 68.9,
  "feels_like_c": 19.0,
  "feels_like_f": 66.2,
  "humidity": 60,
  "description": "clear sky",
  "sunrise": "2023-12-04 07:00:00",
  "sunset": "2023-12-04 16:00:00"
}
```

---

## Running Locally

1. Clone the repository:

```bash
git clone https://github.com/yourusername/weather-app.git
cd weather-app
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set your API key in `key/api_key` or use a `.env` file (optional enhancement).

4. Run FastAPI with Uvicorn:

```bash
uvicorn app.main:app --reload
```

5. Open in browser or Postman:

```
http://127.0.0.1:8000/weather/London
```

---

## Docker

Build and run the container:

```bash
docker build -t weather-app .
docker run -p 8000:8000 weather-app
```

---

## Tests

Run all tests with Pytest:

```bash
pytest tests/
```

Tests include:

* Temperature conversion (`kelvin_to_celsius_fahrenheit`)
* Weather data formatting (`format_weather_data`)
* API request handling (`get_weather` with mocked responses)





