import requests
import os
import pygame
from text_to_voice import Speak
API_WEATHER ='8bbf039e288627aa51a2103223647ded'

def weather(text:str) -> None:
    #Check if day of week / in / at / date in text / Today - tomorrow - day afetr tomorrow - x days later                                                                                                              
    """
    whats the weather in --
    whatst the weather at --
    whats the weather
    whats the weather today in ----
    whats the weather today
    whats the weather tomorrow in ---
    whats the weather tomorrow
    hows the weateher 
    """

    #@Whats the weather for now
    lon = '77.5901'
    lat = '12.9768'
    weather_params = {'lat':lat, 'lon':lon,'units':'metric','appid':API_WEATHER}
    response = requests.get('https://api.openweathermap.org/data/2.5/weather',params=weather_params).json()
    try:
        response_main = response['main']
        temp = response_main['temp']
        feels_like = response_main['feels_like']
        temp_min = response_main['temp_min']
        temp_max = response_main['temp_max']
        Speak(f'The minimum temperature is {temp_min} degrees Celcius. the maximum temperature is {temp_max} degrees Celcius. the temperature currently is {temp} degrees Celcius but it will feel like {feels_like} degrees Celcius.')
    except Exception:
        Speak('Sorry, an error occurred')
        print(response)

#fetch_weather('whats the weather')