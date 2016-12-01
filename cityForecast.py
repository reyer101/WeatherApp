from WeatherAPI import WeatherAPI
from datetime import date
import WeatherConsts as Consts
import TempConverter

api = WeatherAPI(Consts.KEY)


def getCityForecast(city):

    forecast_city = api.getForecastCity(city)

    return getCityTemps(forecast_city)


def getCityTemps(forecast_city):

    forecast = ""

    i = 0
    while(i < 32):

        num_date_list = forecast_city['list'][i]['dt_txt'].split(" ")[0].split("-")

        word_date = date(day=int(num_date_list[2]),
                         month=int(num_date_list[1]),
                         year=int(num_date_list[0])).strftime('%A')


        min_temp = forecast_city['list'][i+1]['main']['temp_min']
        minTempF = TempConverter.convertKtoF(min_temp)

        max_temp = forecast_city['list'][i]['main']['temp_max']
        maxTempF = TempConverter.convertKtoF(max_temp)

        forecast += 'Day: ' + word_date + '\n' \
                 + getCityDescriptions(forecast_city, i) \
                 + 'Lows today are: %.2f F' % minTempF + '\n' \
                 + 'Highs today are: %.2f F' % maxTempF + '\n' + '\n' \

        i=i+8

    return forecast

def getCityDescriptions(forecast_city, i):

    description = forecast_city['list'][i]['weather'][0]['description'].title()
    return 'Sky Description: ' + description + '\n'




