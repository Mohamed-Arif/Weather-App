import requests
from flask import Flask, render_template, request

app = Flask(__name__)

API_KEY = '7d2ccf162636befe1223b1483251a6ab'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['cityInput']
        weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

        response = requests.get(weather_url)
        data = response.json()
        current_temperature = data['main']['temp']

        return str(current_temperature)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)



# import requests
# from flask import Flask, render_template

# app = Flask(__name__)

# API_KEY = '7d2ccf162636befe1223b1483251a6ab'
# city = 'London'
# weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
# forecast_url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'

# @app.route('/')
# def index():
#     # Get the current weather data
#     weather_response = requests.get(weather_url)
#     weather_data = weather_response.json()
#     current_temperature = weather_data['main']['temp']

#     # Get the forecast data for the next day
#     forecast_response = requests.get(forecast_url)
#     forecast_data = forecast_response.json()
#     next_day_forecast = forecast_data['list'][8]['main']['temp']

#     return render_template('index.html', current_temperature=current_temperature, next_day_forecast=next_day_forecast)

# if __name__ == '__main__':
#     app.run(debug=True)
# gbgsgbsbgsukbg
