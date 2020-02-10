import requests

# Format for weather conditions i.e to be displayed in the label...
def format_Weather(weather):
    try:
        city = weather['name']
        conditions = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (city, conditions, temp)
    except:
        final = 'There is no such city...'
        
    return final    
#...    

# Gets the weather report of that city...
def get_weather(city):
    weather_key = '51964a5ddd02d7b577fcea43e9ceb81a'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    param = {'APPID':weather_key, 'q':city, 'units':'metric'}
    response = requests.get(url, params = param)
    weather = response.json()
    text = format_Weather(weather)
    return text
#... 
