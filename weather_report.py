import os, requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = os.getenv("WEATHER_API_BASE")

class WeatherAPIError(Exception):
    pass

def get_weather_report(city: str, units: str = "metric"):
    if not city:
        raise ValueError("City name cannot be empty.")

    params = {
        "q":city,
        "appid":API_KEY,
        "units":units
    }

    try:
        response = requests.get(f"{BASE_URL}/weather", params=params)
        response.raise_for_status()
        data = response.json()
        # print(data)

        weather = {
            "city": data.get("name"),
            "country": data.get("sys", {}).get("country"),
            "temperature": data.get("main", {}).get("temp"),
            "feels_like": data.get("main", {}).get("feels_like"),
            "humidity": data.get("main", {}).get("humidity"),
            "wind_speed": data.get("wind", {}).get("speed"),
            "condition": data.get("weather", [{}])[0].get("main"),
            "description": data.get("weather", [{}])[0].get("description"),
        }

        if not weather['city']:
            raise WeatherAPIError("Invalid city")

        return weather

    except requests.exceptions as e:
        raise WeatherAPIError(f"An error occured {e}")

# get_weather_report("Jaipur")