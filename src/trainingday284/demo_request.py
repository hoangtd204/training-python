import requests

api_key = "c5d69b339e0edb9d2cdb25b9eba3c361"
city = "Hanoi"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    temp_kelvin = data['main']['temp']
    temp_celsius = temp_kelvin - 273.15

    weather_desc = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    print("\n== RESPONSE ==")

    print("Endpoint (URL):", response.request.url)
    print("HTTP Method:", response.request.method)
    print("Status Code:", response.status_code)
    print("Response Headers:")
    for key, value in response.headers.items():
        print(f"  {key}: {value}")

    print(f"Weather in {city}: {weather_desc}")
    print(f"Temperature: {temp_celsius:.2f}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print(f"Error: {response.status_code} - Unable to retrieve weather data")
