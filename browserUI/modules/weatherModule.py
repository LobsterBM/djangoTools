import time

import requests
"""
LAT= settings.LAT
LON = settings.LON
WEATHER_API = settings.WEATHER_API
WEATHER_URL1 = settings.WEATHER_URL1
WEATHER_URL2 = settings.WEATHER_URL2
WEATHER_URL3 = settings.WEATHER_URL3
LOCATION = settings.LOCATION
"""

weatherColor = {
    2 : ["white","on_grey"],
    3 : ["cyan" , "on_blue"],
    5 : ["cyan", 'on_blue'],
    6 : ["white", "on_white"],
    7 : ["magenta", "on_cyan"],
    800 : ["blue", "on_cyan"],
    801 : ["cyan", "on_cyan"],
    802 : ["white","on_grey"],
    803 : ["white","on_grey"],
    804 : ["white","on_grey"]
}

class Weather :
    def __init__(self, temp , wind , weather,id,color,bgcolor):
        self.temp = temp
        self.wind = wind
        self.weather = weather
        self.id = id
        self.color = color
        self.bgcolor = bgcolor



def weatherModule(settings , LOCK , timer , x,y, hours):
    LAT = settings.LAT
    LON = settings.LON
    WEATHER_API = settings.WEATHER_API
    WEATHER_URL1 = settings.WEATHER_URL1
    WEATHER_URL2 = settings.WEATHER_URL2
    WEATHER_URL3 = settings.WEATHER_URL3
    LOCATION = settings.LOCATION

    # 600s for 10 minutes
    #TODO make update possible
    newRequest = 0


    if hours > 12:
        hours = 12
    weatherURL =  WEATHER_URL1 + str(LAT) + WEATHER_URL2 + str(LON) + WEATHER_URL3 + WEATHER_API
    weatherData = requests.get(weatherURL).json()

    while True :
        if newRequest == 0 :
            weatherData = requests.get(weatherURL).json()

        hourList = weatherData['hourly']
        hourlyWeather = []

        for i in hourList :
            id = int(i['weather'][0]['id'])
            if id<800 :
                color = weatherColor[id//100]
            else:
                color = weatherColor[id]
            hourlyWeather.append(Weather(i['temp'] , i['wind_speed'] , i['weather'][0]['main'], id, color[0] , color[1]))

        weatherTable = [["Time","Temp" , "Weather" , "Wind"]]
        currentHour = int(time.strftime("%H"))

        for i in range(hours) :
            listElem=["{:0>2n}:00".format(currentHour), str(hourlyWeather[i].temp)+"°" , colored(str(hourlyWeather[i].weather), hourlyWeather[i].color,attrs=['bold']) , str(hourlyWeather[i].wind)+" km/h"]
            weatherTable.append(listElem)
            currentHour+=1
            currentHour = currentHour%24


        table_instance = terminaltables.SingleTable(weatherTable, "Weather : " + LOCATION)
        table_instance.justify_columns[3] = 'center'

        LOCK.acquire()
        move(x, y)
        print(table_instance.table)
        print()
        LOCK.release()

        newRequest -=1
        newRequest %= timer

        time.sleep(timer)




    return