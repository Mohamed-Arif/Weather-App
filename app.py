from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = '<7d2ccf162636befe1223b1483251a6ab>'
city = 'London'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'


@app.route('/')
def index():
    response = requests.get(url)
    data = response.json()
    temperature = data['main']['temp']
    print(f"The current temperature in {city} is {temperature}°C")
    return render_template('index.html', temperature=temperature)

if __name__ == '__main__':
    app.run(debug=True)




