from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '7d2ccf162636befe1223b1483251a6ab'

@app.route("/", methods=["GET", "POST"])
def get_weather():
    if request.method == "POST":
        city = request.form["city"]
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        weather_data = response.json()
        temperature = weather_data["main"]["temp"]
        return render_template("index.html", temperature=temperature, city=city)
    else:
        url = f"http://api.openweathermap.org/data/2.5/weather?q=London&appid={API_KEY}&units=metric"
        response = requests.get(url)
        weather_data = response.json()
        temperature = weather_data["main"]["temp"]
        return render_template("index.html", temperature=temperature, city='London')

if __name__ == '__main__':
    app.run(debug=True)
