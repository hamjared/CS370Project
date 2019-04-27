# -*- coding: utf-8 -*-
from django.shortcuts import render
import ESP8266Coms


def index(request):
    weather = {
        'city': "Ft Collins",
        'temperature': ESP8266Coms.getTemp(),
        'humidity': ESP8266Coms.getHumidity(),
        'pressure': ESP8266Coms.getPressure(),
        'description': "Sunny"
    }
    context = {'weather': weather}
    return render(request, 'weather/index.html', context) #returns the index.html template

