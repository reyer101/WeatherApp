from WeatherAPI import WeatherAPI
import WeatherConsts as Consts
import TempConverter
import TimeConverter


def main():
    api = WeatherAPI(Consts.KEY)

    print ('Enter the name of your city for current weather')
    city = raw_input('City: ')

    weather = api.getWeather(city)

    print (weather)

    #Gets the current time and formats it like 02:00pm
    time = TimeConverter.current_time()

    sunset_time = TimeConverter.time_convert(weather['sys']['sunset'])
    sunrise_time = TimeConverter.time_convert(weather['sys']['sunrise'])

    temperature = weather['main']['temp']
    tempF = TempConverter.convertKtoF(temperature)
    print ('Current time: ' + time)
    print ('Sunrise: ' + sunrise_time)
    print ('Sunset: ' + sunset_time)
    print ('Current temperature in Fahrenheit: ')
    print ("%.2f" % tempF)
    tempC = TempConverter.convertKtoC(temperature)
    print ('Current temperature in Celsius: ')
    print ("%.2f" % tempC)
if __name__ == "__main__":
    main()

