"""
Day 12 Deliverable: Weather CLI — OpenWeatherMap API with full error handling
Covers: GET requests, params, raise_for_status, timeout, error hierarchy
"""
import os
import requests
from dotenv import load_dotenv
from dataclasses import dataclass


load_dotenv()

API_KEY  = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5"


# ── Custom Exceptions ─────────────────────────────────────────────────────

class WeatherError(Exception):
    """Base exception for weather API errors."""
    pass

class CityNotFoundError(WeatherError):
    """Raised when city does not exist."""
    pass

class APIKeyError(WeatherError):
    """Raised when API key is invalid or missing."""
    pass


# ── Data Structure ────────────────────────────────────────────────────────

@dataclass
class WeatherData:
    city:        str
    country:     str
    temperature: float
    feels_like:  float
    humidity:    int
    description: str
    wind_speed:  float

    def __str__(self) -> str:
        return (
            f"\n{'='*40}\n"
            f"  {self.city}, {self.country}\n"
            f"{'='*40}\n"
            f"  Temperature : {self.temperature}°C\n"
            f"  Feels like  : {self.feels_like}°C\n"
            f"  Humidity    : {self.humidity}%\n"
            f"  Wind speed  : {self.wind_speed} m/s\n"
            f"  Condition   : {self.description.title()}\n"
            f"{'='*40}"
        )


# ── API Client ────────────────────────────────────────────────────────────

def fetch_weather(city: str, units: str = "metric") -> WeatherData:
    """
    Fetch current weather for a city.
    Raises WeatherError subclasses on failure.
    """
    if not API_KEY:
        raise APIKeyError("OPENWEATHER_API_KEY not set in .env")

    params = {
        "q":     city,
        "appid": API_KEY,
        "units": units,
    }

    try:
        response = requests.get(
            f"{BASE_URL}/weather",
            params=params,
            timeout=10
        )
        response.raise_for_status()

    except requests.exceptions.ConnectionError:
        raise WeatherError("No internet connection — check your network.")

    except requests.exceptions.Timeout:
        raise WeatherError("Request timed out — try again.")

    except requests.exceptions.HTTPError as e:
        status = e.response.status_code
        if status == 401:
            raise APIKeyError("Invalid API key — check your .env file.")
        elif status == 404:
            raise CityNotFoundError(f"City not found: {city!r}")
        elif status == 429:
            raise WeatherError("Rate limit exceeded — wait before retrying.")
        else:
            raise WeatherError(f"HTTP {status}: {e.response.text}")

    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        raise WeatherError("Invalid JSON response from API.")

    return WeatherData(
        city=        data["name"],
        country=     data["sys"]["country"],
        temperature= data["main"]["temp"],
        feels_like=  data["main"]["feels_like"],
        humidity=    data["main"]["humidity"],
        description= data["weather"][0]["description"],
        wind_speed=  data["wind"]["speed"],
    )


def compare_cities(cities: list[str]) -> None:
    """Fetch and display weather for multiple cities."""
    results: list[WeatherData] = []

    for city in cities:
        try:
            weather = fetch_weather(city)
            results.append(weather)
        except CityNotFoundError as e:
            print(f"Skipping — {e}")
        except WeatherError as e:
            print(f"Error for {city}: {e}")

    if not results:
        print("No valid results.")
        return

    # Sort by temperature descending
    results.sort(key=lambda w: w.temperature, reverse=True)

    print(f"\n{'City':<20} {'Temp':>8} {'Humidity':>10} {'Wind':>8}")
    print("-" * 50)
    for w in results:
        print(f"{w.city:<20} {w.temperature:>7.1f}°C {w.humidity:>9}% {w.wind_speed:>6.1f}m/s")


# ── CLI ───────────────────────────────────────────────────────────────────

def main() -> None:
    if not API_KEY:
        print("ERROR: OPENWEATHER_API_KEY not found in .env")
        return

    print("=== Weather CLI ===")
    print("Commands: single city | 'compare' | 'quit'")

    while True:
        user_input = input("\nEnter city (or command): ").strip()

        if not user_input:
            continue

        if user_input.lower() == "quit":
            print("Goodbye.")
            break

        elif user_input.lower() == "compare":
            raw = input("Enter cities separated by comma: ")
            cities = [c.strip() for c in raw.split(",") if c.strip()]
            compare_cities(cities)

        else:
            try:
                weather = fetch_weather(user_input)
                print(weather)
            except CityNotFoundError as e:
                print(f"Not found: {e}")
            except APIKeyError as e:
                print(f"API key error: {e}")
                break
            except WeatherError as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    main()