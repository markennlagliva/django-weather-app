from django.shortcuts import render
import requests

# env variables
from dotenv import load_dotenv
import os

def weather(request):

    load_dotenv()
    weather_api = os.getenv('WEATHER_API')
    api_endpoint = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

    if request.method == 'POST':
        try: 
            city = request.POST.get('city')
            weather_data = requests.get(api_endpoint.format(city, weather_api)).json()
            celsius = round(int(weather_data['main']['temp']) - 273.15,2)
            for data in weather_data['weather']:
                weather_description, weather_main = data['description'], data['main']
                # Do if-else statement
                # 1. Return result (img status and gif background names)
                # 2. For no result data, img with "no result!".
                print(weather_main)

                if weather_main == 'Clear':
                    img = 'clear-sky.png'
                    img_bg = 'clear-sky.gif'
                elif weather_main == 'Clouds':
                    img = 'cloudy.png'
                    img_bg = 'cloudy.gif'
                elif weather_main == 'Rain':
                    img = 'rain.png'
                    img_bg = 'rain.gif'
                elif weather_main == 'Drizzle':
                    img = 'drizzle.png'
                    img_bg = 'drizzle.gif'
                elif weather_main == 'Thunderstorm':
                    img = 'thunderstorm.png'
                    img_bg = 'thunderstorm.gif'
                elif weather_main == 'Snow':
                    img = 'snow.png'
                    img_bg = 'snow.gif'
                elif weather_main == 'Mist':
                    img = 'mist.png'
                    img_bg = 'mist.gif'
                elif weather_main == 'Fog':
                    img = 'fog.png'
                    img_bg = 'fog.gif'
                elif weather_main == 'Smoke':
                    img = 'smoke.png'
                    img_bg = 'smoke.gif'
                elif weather_main == 'Haze':
                    img = 'haze.png'
                    img_bg = 'haze.gif' 
        except:
            return render(request, 'base.html', {'notFound': 'notFound'})
         
        return render(request, 'base.html', {'weather_data': weather_data, 'celcius': celsius, 'weather_description': weather_description, 'img': img, 'img_bg': img_bg})
   
    return render(request, 'base.html')