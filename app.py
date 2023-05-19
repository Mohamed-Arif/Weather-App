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
