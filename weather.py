import requests
import pandas as pd


city = input('Enter the name of the city: ')

def get_weather(city):
    api = 'your_api_key'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric'
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame({
        'City': [data['name']],
        'Country': [data['sys']['country']],
        'Temperature': [data['main']['temp']],
        'MIN Temperature': [data['main']['temp_min']],
        'MAX Temperature': [data['main']['temp_max']],
        'Humidity': [data['main']['humidity']],
        'Pressure': [data['main']['pressure']],
        'Clouds': [data['clouds']['all']]
    })
    return df


weather_data = get_weather(city)
print(weather_data)
