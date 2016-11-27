from WeatherAPI import WeatherAPI
import WeatherConsts as Consts
import TempConverter
import TimeConverter
import convert2cardinal

def cityWeather(city, api_key):
    #city_api_key = api_key;
    weather = api_key.getWeatherCity(city)
    print (weather)

    ## weather['wind']['deg']

    #Gets the current time and formats it like 02:00pm
    time = TimeConverter.current_time()

    sunset_time = TimeConverter.time_convert(weather['sys']['sunset'])
    sunrise_time = TimeConverter.time_convert(weather['sys']['sunrise'])

    temperature = weather['main']['temp']
    tempF = TempConverter.convertKtoF(temperature)

    print ('\nCurrent time: ' + time)
    print ('Sunrise: ' + sunrise_time)
    print ('Sunset: ' + sunset_time)

    print ('Current temperature in Fahrenheit: %.2f F' % tempF)

    tempC = TempConverter.convertKtoC(temperature)
    print ('Current temperature in Celsius: %.2f C' % tempC)

    description = weather['weather'][0]['description'].title()
    print ('Sky description: ' + description)

    minTemperature = weather['main']['temp_min']
    minTempF = TempConverter.convertKtoF(minTemperature)
    minTempC = TempConverter.convertKtoC(minTemperature)
    print ('Lows today are: %.2f F' % minTempF)
    print ('Lows today are: %.2f C' % minTempC)
    maxTemperature = weather['main']['temp_max']
    maxTempF = TempConverter.convertKtoF(maxTemperature)
    maxTempC = TempConverter.convertKtoC(maxTemperature)
    print ('Highs today are: %.2f F' % maxTempF)
    print ('Highs today are: %.2f C' % maxTempC)

    humidity = weather['main']['humidity']
    print ('Humidity: ' + str (humidity) + '%')

    #Wind speed measured in meters per second (mps)
    windSpeed = weather['wind']['speed']*2.23694
    print ('Wind Speed: %.2f' % (windSpeed) + " mph")

    #If deg is not given, does not work
    windDirection = weather['wind']['deg']

    #converts direction to NE, E, SE, S, SW, W, NW, or, N
    print ('Wind Direction: ' + convert2cardinal.convert2cardinal(windDirection))

def zipWeather(zip_code, api_key):
    #zip_api_key = api_key;
    weather = api_key.getWeatherZip(zip_code)
    print (weather)

    ## weather['wind']['deg']

    #Gets the current time and formats it like 02:00pm
    time = TimeConverter.current_time()

    sunset_time = TimeConverter.time_convert(weather['sys']['sunset'])
    sunrise_time = TimeConverter.time_convert(weather['sys']['sunrise'])

    temperature = weather['main']['temp']
    tempF = TempConverter.convertKtoF(temperature)

    print ('\nCurrent time: ' + time)
    print ('Sunrise: ' + sunrise_time)
    print ('Sunset: ' + sunset_time)

    print ('Current temperature in Fahrenheit: %.2f F' % tempF)

    tempC = TempConverter.convertKtoC(temperature)
    print ('Current temperature in Celsius: %.2f C' % tempC)

    description = weather['weather'][0]['description'].title()
    print ('Sky description: ' + description)

    minTemperature = weather['main']['temp_min']
    minTempF = TempConverter.convertKtoF(minTemperature)
    minTempC = TempConverter.convertKtoC(minTemperature)
    print ('Lows today are: %.2f F' % minTempF)
    print ('Lows today are: %.2f C' % minTempC)
    maxTemperature = weather['main']['temp_max']
    maxTempF = TempConverter.convertKtoF(maxTemperature)
    maxTempC = TempConverter.convertKtoC(maxTemperature)
    print ('Highs today are: %.2f F' % maxTempF)
    print ('Highs today are: %.2f C' % maxTempC)

    humidity = weather['main']['humidity']
    print ('Humidity: ' + str (humidity) + '%')

    #Wind speed measured in meters per second (mps)
    windSpeed = weather['wind']['speed']*2.23694
    print ('Wind Speed: %.2f' % (windSpeed) + " mph")

    #If deg is not given, does not work
    windDirection = weather['wind']['deg']

    #converts direction to NE, E, SE, S, SW, W, NW, or, N
    print ('Wind Direction: ' + convert2cardinal.convert2cardinal(windDirection))

def main():
    api = WeatherAPI(Consts.KEY)

    print ('Enter the name of your city for current weather')
    city = raw_input('City: ')
    cityWeather(city, api);
    #weather = api.getWeatherCity(city)

    weather_zip = api.getWeatherZip(94040)
    print ('\n')
    #print (weather)

    #print (weather_zip)

    print ('Enter the zip code of another city')
    zip_code = raw_input('Zip code: ')
    zipWeather(zip_code, api)
    ## weather['wind']['deg']

if __name__ == "__main__":
    main()
