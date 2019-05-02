# -*- coding: utf-8 -*-
from django.shortcuts import render
import ESP8266Coms
import location


def index(request):
    coords = location.getCoords()
    formattedCoords = "({:.4f}, {:.4f})".format(coords['location']['lat'],coords['location']['lng'])
    city_state = location.getCity(coords)
    temp = ESP8266Coms.getTemp()
    humidity = ESP8266Coms.getHumidity()
    pressure = ESP8266Coms.getPressure()
    sunlight = ESP8266Coms.getSolar()

    if temp < 40:
        description = "Cold"
    elif temp < 60:
        description = "Cool"
    elif temp < 70:
        description = "Warm"
    else:
        description = "Hot"


    weather = {
        'city': city_state,
        'temperature': temp,
        'humidity': humidity,
        'pressure': pressure,
        'description': description,
        'coords': formattedCoords,
        'Sunlight': sunlight
    }
    context = {'weather': weather}
    return render(request, 'weather/index.html', context) #returns the index.html template

