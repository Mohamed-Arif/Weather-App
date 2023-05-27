import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

API_KEY = '7d2ccf162636befe1223b1483251a6ab'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['cityInput']
        weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

        try:
            response = requests.get(weather_url)
            data = response.json()
            current_temperature = data['main']['temp']
            feels_like_temperature = data['main']['feels_like']
            return jsonify({
                'currentTemperature': current_temperature,
                'feelsLikeTemperature': feels_like_temperature
            })
        except KeyError:
            return 'Invalid city name or weather data not available'
        except requests.exceptions.RequestException as e:
            return f'Error occurred: {str(e)}'

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)



# import requests
# from flask import Flask, render_template, request

# app = Flask(__name__)

# API_KEY = '7d2ccf162636befe1223b1483251a6ab'

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         city = request.form['cityInput']
#         weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

#         response = requests.get(weather_url)
#         data = response.json()
#         current_temperature = data['main']['temp']

#         return str(current_temperature)

#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)
