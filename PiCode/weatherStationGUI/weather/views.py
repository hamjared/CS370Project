# -*- coding: utf-8 -*-
from django.shortcuts import render
import ESP8266Coms


def index(request):
    weather = {
        'city': "Ft Collins",
        'temperature': ESP8266Coms.getTemp(),
        'humidity': ESP8266Coms.getHumidity(),
        'description': "Sunny"
    }
    context = {'weather': weather}
    return render(request, 'weather/index.html', context) #returns the index.html template

