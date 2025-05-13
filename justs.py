import requests

API_KEY = "7f9df110ecc0aae10af67b778b0aed49"  # Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

city = input("Enter city name: ")
url = BASE_URL + "appid=" + API_KEY + "&q=" + city + "&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    main = data['main']
    weather = data['weather'][0]

    print(f"\nWeather in {city.title()}:")
    print(f"Temperature: {main['temp']}°C")
    print(f"Feels like: {main['feels_like']}°C")
    print(f"Humidity: {main['humidity']}%")
    print(f"Condition: {weather['description'].title()}")
else:
    print("City not found. Please check the name.")


