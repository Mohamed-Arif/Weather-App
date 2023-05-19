# Weather App

The Weather App is a simple web application that displays the current temperature and forecast for a specific city. It retrieves weather data from the OpenWeatherMap API and presents it in a user-friendly format.

## Features

- Displays the current temperature in Celsius for a default city (London).
- Allows users to search for weather information in different cities.
- Shows the forecast for the next day.
- Stylish user interface with a background image and custom styling.

## Prerequisites

To run the Weather App, you need to have the following:

- Python 3 installed on your machine.
- Flask library installed. You can install it by running `pip install flask`.
- An OpenWeatherMap API key. You can sign up for a free API key on the [OpenWeatherMap website](https://openweathermap.org/) and replace the `API_KEY` variable in `app.py` with your key.

## Installation and Usage

1. Clone the repository to your local machine or download the source code.
2. Open a terminal or command prompt and navigate to the project directory.
3. Install the required dependencies by running `pip install -r requirements.txt`.
4. Set your OpenWeatherMap API key by replacing the `API_KEY` variable in `app.py` with your key.
5. Start the Flask development server by running `python app.py`.
6. Open a web browser and enter `http://localhost:5000` in the address bar.
7. The Weather App should now be running, and you can view the weather information for the default city or search for different cities.

## Customization

You can customize the Weather App by modifying the following files:

- `app.py`: Update the default city or modify the API endpoints for different weather data.
- `index.html`: Adjust the HTML structure and layout of the web page.
- `style.css`: Modify the CSS styles to change the appearance of the app.

Feel free to experiment and make the app your own!

## Contributing

Contributions to the Weather App are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).

