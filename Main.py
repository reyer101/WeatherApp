from WeatherAPI import WeatherAPI
import WeatherConsts as Consts
import TempConverter


def main():
    api = WeatherAPI(Consts.KEY)

    print ('Enter the name of your city for current weather')
    city = raw_input('City: ')

    weather = api.getWeather(city)

    print (weather)

    temperature = weather['main']['temp']
    tempF = TempConverter.convertKtoF(temperature)
    print ('Current temperature in Fahrenheit: %.2f F' % tempF)
    tempC = TempConverter.convertKtoC(temperature)
    print ('Current temperature in Celsius: %.2f C' % tempC)

    minTemperature = weather['main']['temp_min']
    minTempF = TempConverter.convertKtoF(minTemperature)
    print ('Lows today are: %.2f F' % minTempF)
    maxTemperature = weather['main']['temp_max']
    maxTempF = TempConverter.convertKtoF(maxTemperature)
    print ('Highs today are: %.2f F' % maxTempF)
if __name__ == "__main__":
    main()

