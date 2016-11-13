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

    print ('Current temperature in Fahrenheit: %.2f F' % tempF)

    tempC = TempConverter.convertKtoC(temperature)
    print ('Current temperature in Celsius: %.2f C' % tempC)
    
    description = weather['weather'][0]['description'].title()
    print ('Sky description: ' + description)

    minTemperature = weather['main']['temp_min']
    minTempF = TempConverter.convertKtoF(minTemperature)
    print ('Lows today are: %.2f F' % minTempF)
    maxTemperature = weather['main']['temp_max']
    maxTempF = TempConverter.convertKtoF(maxTemperature)
    print ('Highs today are: %.2f F' % maxTempF)

    humidity = weather['main']['humidity']
    print ('Humidity: ' + str (humidity) + '%')
    
    #Wind speed measured in meters per second (mps)
    windSpeed = weather['wind']['speed']*2.23694
    print ('Wind Speed: %.2f' % (windSpeed) + " mph")
    
    #If deg is not given, does not work
    windDirection = weather['wind']['deg']

    if windDirection > 22.5 and windDirection < 67.5:
        cardinalDirection = 'NE'
    elif windDirection > 67.6 and windDirection < 112.5:
        cardinalDirection = 'E'
    elif windDirection > 112.6 and windDirection < 157.5:
        cardinalDirection = 'SE'
    elif windDirection > 157.6 and windDirection < 202.5:
        cardinalDirection = 'S'
    elif windDirection > 202.6 and windDirection < 247.5:
        cardinalDirection = 'SW'
    elif windDirection > 247.6 and windDirection < 292.5:
        cardinalDirection = 'W'
    elif windDirection > 292.6 and windDirection < 337.5:
        cardinalDirection = 'NW'
    else:
        cardinalDirection = 'N'
    print ('Wind Direction: ' + cardinalDirection)
    
if __name__ == "__main__":
    main()

