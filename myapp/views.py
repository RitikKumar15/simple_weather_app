from django.shortcuts import render
import requests

def get_data(city):
  #api_key = '9957636924b836b2ced5f5782ada2ecf'
  response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=3c855746ea6235d81404c2310e1451f2")
  json_data = response.json()
  return json_data

def weather_details(request):
  weather = False
  if request.method == 'POST':
    city = request.POST.get('city')
    data = get_data(city)
    weather = dict()
    weather['lon'] = data['coord']['lon']
    weather['lat'] = data['coord']['lat']
    weather['desc'] = data['weather'][0]['main']
    weather['temp'] = data['main']['temp']
    weather['temp_min'] = data['main']['temp_min']
    weather['temp_max'] = data['main']['temp_max']
    weather['pressure'] = data['main']['pressure']
    weather['humidity'] = data['main']['humidity']
    weather['visibility'] = data['visibility']
    weather['wind_speed'] = data['wind']['speed']
    weather['country'] = data['sys']['country']
    weather['city_name'] = data['name']
  return render(request, 'myapp/index.html', {'weather': weather})