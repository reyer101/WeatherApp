from WeatherAPI import WeatherAPI
from datetime import date
import WeatherConsts as Consts
import TempConverter
import TimeConverter

api = WeatherAPI(Consts.KEY)


def getCityForecast():

    print('Enter the name of your city for a 5 day forecast: ')

    city = raw_input("City: ")

    forecast_city = api.getForecastCity(city)

    getCityTemps(forecast_city)


def getCityTemps(forecast_city):

    i = 0
    while(i < 40):

        num_date_list = forecast_city['list'][i]['dt_txt'].split(" ")[0].split("-")

        word_date = date(day=int(num_date_list[2]),
                         month=int(num_date_list[1]),
                         year=int(num_date_list[0])).strftime('%A')

        print "Day: " + word_date
        getCityDescriptions(forecast_city, i)

        min_temp = forecast_city['list'][i]['main']['temp_min']
        minTempF = TempConverter.convertKtoF(min_temp)

        max_temp = forecast_city['list'][i]['main']['temp_max']
        maxTempF = TempConverter.convertKtoF(max_temp)

        print ('Lows today are: %.2f F' % minTempF)
        print ('Highs today are: %.2f F' % maxTempF)

        print(" ")

        i=i+8

def getCityDescriptions(forecast_city, i):

    description = forecast_city['list'][i]['weather'][0]['description'].title()
    print("Sky Description: " + description)




