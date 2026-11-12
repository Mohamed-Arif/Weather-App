import os

import requests
from flask import Flask, jsonify, render_template, request

try:  # optional: load OPENWEATHER_API_KEY from a .env file
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

app = Flask(__name__)

API_KEY = os.environ.get("OPENWEATHER_API_KEY")
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
AIR_URL = "https://api.openweathermap.org/data/2.5/air_pollution"
AQI_LABELS = {1: "Good", 2: "Fair", 3: "Moderate", 4: "Poor", 5: "Very poor"}
TIMEOUT = 10


def error(message, status):
    return jsonify({"error": message}), status


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", default_city=os.environ.get("DEFAULT_CITY", "London"))


@app.route("/", methods=["POST"])
@app.route("/weather", methods=["POST"])
def weather():
    if not API_KEY:
        return error("The server has no OpenWeatherMap API key. Set OPENWEATHER_API_KEY and restart.", 500)

    city = (request.form.get("cityInput") or "").strip()
    if not city:
        return error("Enter a city name.", 400)

    try:
        resp = requests.get(WEATHER_URL, params={"q": city, "appid": API_KEY, "units": "metric"}, timeout=TIMEOUT)
        if resp.status_code == 404:
            return error(f"Couldn't find a city called “{city}”.", 404)
        if resp.status_code == 401:
            return error("The OpenWeatherMap API key was rejected. Check OPENWEATHER_API_KEY.", 502)
        resp.raise_for_status()
        data = resp.json()

        # Air quality comes from a separate endpoint, looked up by coordinates
        aqi = None
        coord = data.get("coord", {})
        if "lat" in coord and "lon" in coord:
            try:
                air = requests.get(AIR_URL, params={"lat": coord["lat"], "lon": coord["lon"], "appid": API_KEY}, timeout=TIMEOUT)
                air.raise_for_status()
                aqi = air.json()["list"][0]["main"]["aqi"]
            except (requests.RequestException, KeyError, IndexError):
                aqi = None

        return jsonify({
            "city": data.get("name", city),
            "country": data.get("sys", {}).get("country", ""),
            "description": (data.get("weather") or [{}])[0].get("description", ""),
            "currentTemperature": round(data["main"]["temp"]),
            "feelsLikeTemperature": round(data["main"]["feels_like"]),
            "airQualityIndex": aqi,
            "airQualityLabel": AQI_LABELS.get(aqi, "Not available"),
            "sunriseTime": data.get("sys", {}).get("sunrise"),
            "sunsetTime": data.get("sys", {}).get("sunset"),
            "timezoneOffset": data.get("timezone", 0),  # seconds from UTC, for the city's local time
        })
    except requests.RequestException:
        return error("Couldn't reach OpenWeatherMap. Try again in a moment.", 502)
    except (KeyError, ValueError):
        return error("OpenWeatherMap sent an unexpected response.", 502)


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")
