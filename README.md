# Weather App

A small Flask web app that shows the current weather for any city, using the [OpenWeatherMap](https://openweathermap.org/) API.

## Features

- Search any city by name; the page opens on a default city (London unless you change it)
- Current temperature and "feels like" temperature in °C, plus a short description (e.g. *haze*)
- Air quality index from 1 (Good) to 5 (Very poor), from OpenWeatherMap's air pollution data
- Sunrise and sunset in the **city's own local time**
- Clear messages for unknown cities, network problems or a missing API key

## Setup

Needs Python 3.8 or newer and a free OpenWeatherMap API key ([sign up here](https://home.openweathermap.org/users/sign_up)). New keys can take an hour or two to start working.

```bash
git clone https://github.com/Mohamed-Arif/Weather-App.git
cd Weather-App
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and put your key in it:

```
OPENWEATHER_API_KEY=your-key-here
DEFAULT_CITY=London
```

`.env` is in `.gitignore`, so your key never ends up on GitHub. You can also set `OPENWEATHER_API_KEY` as an ordinary environment variable instead.

## Run

```bash
python app.py
```

Then open http://localhost:5000.

For development with auto-reload and error pages, set `FLASK_DEBUG=1` first. Leave it off anywhere other people can reach the app.

## How it works

- `app.py` serves the page and a `POST /weather` endpoint. It calls OpenWeatherMap's current weather API, then the air pollution API using the city's coordinates, and returns one JSON object.
- `templates/index.html` sends the search and fills in the page. Times are converted using the city's UTC offset from the API, so sunrise in Tokyo shows Tokyo time wherever you are.

## Licence

MIT. See [LICENSE](LICENSE).
