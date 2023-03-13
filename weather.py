import requests
import pandas as pd


city = input('Введіть назву міста: ')

def get_weather(city):
    api = '17e5e96ced879e47af884821a64775e3'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric'
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame({
        'Місто': [data['name']],
        'Країна': [data['sys']['country']],
        'Температура': [data['main']['temp']],
        'Мінімальна температура': [data['main']['temp_min']],
        'Максимальна температура': [data['main']['temp_max']],
        'Вологість': [data['main']['humidity']],
        'Тиск': [data['main']['pressure']],
        'Хмарність': [data['clouds']['all']]
    })
    return df


weather_data = get_weather(city)
print(weather_data)