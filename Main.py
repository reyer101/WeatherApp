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
    print ('Current temperature in Fahrenheit: ')
    print ("%.2f" % tempF)
    tempC = TempConverter.convertKtoC(temperature)
    print ('Current temperature in Celsius: ')
    print ("%.2f" % tempC)
if __name__ == "__main__":
    main()

