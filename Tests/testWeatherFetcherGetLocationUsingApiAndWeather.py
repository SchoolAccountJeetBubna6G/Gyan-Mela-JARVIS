def test():
    import requests

    geo_params = {'q':'Bangaluru', 'appid':'3838a3abfc92026ddcf76dca249ced98'}
    geo_location = requests.get('http://api.openweathermap.org/geo/1.0/direct', params=geo_params)
    geo_location = geo_location.json()
    print(geo_location)
    lat = geo_location[0]['lat'] #77.5901
    lon = geo_location[0]['lon'] #12.9768

    weather_params = {'lat':lat, 'lon':lon,'units':'metric','appid':'3838a3abfc92026ddcf76dca249ced98'}
    weather_data = requests.get('https://api.openweathermap.org/data/2.5/weather', params=weather_params)
    print(weather_data.json())

test()