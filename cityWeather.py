from WeatherAPI import WeatherAPI
import WeatherConsts as Consts
import TempConverter
import TimeConverter
import convert2cardinal


api_key = WeatherAPI(Consts.KEY)


#prints weaather by city
def cityWeather(city):

    weather_city = api_key.getWeatherCity(city)

    return cityTimes(weather_city) + cityTemps(weather_city) + cityDescription(weather_city)+ '\n'

def cityTemps(weather_city):
    temperature = weather_city['main']['temp']
    tempF = TempConverter.convertKtoF(temperature)
    tempC = TempConverter.convertKtoC(temperature)
    
    minTemperature = weather_city['main']['temp_min']
    minTempF = TempConverter.convertKtoF(minTemperature)
    minTempC = TempConverter.convertKtoC(minTemperature)
    
    maxTemperature = weather_city['main']['temp_max']
    maxTempF = TempConverter.convertKtoF(maxTemperature)
    maxTempC = TempConverter.convertKtoC(maxTemperature)

    return 'Current temperature in Fahrenheit: %.2f F' % tempF + '\n' \
           + 'Current temperature in Celsius: %.2f C' % tempC + '\n' \
           + 'Highs today are: %.2f F' % maxTempF + '\n' \
           + 'Highs today are: %.2f C' % maxTempC + '\n' \
           + 'Lows today are: %.2f F' % minTempF + '\n' \
           + 'Lows today are: %.2f C' % minTempC + '\n'

#prints sunrise, sunset, and current time by city name
def cityTimes(weather_city):
    #Gets the current time and formats it like 02:00pm
    time = TimeConverter.current_time()
    
    #Gets sunset and sunrise times
    sunset_time = TimeConverter.time_convert(weather_city['sys']['sunset'])
    sunrise_time = TimeConverter.time_convert(weather_city['sys']['sunrise'])
    

    return 'Current time: ' + time + '\n' \
         + 'Sunrise: ' + sunrise_time + '\n' \
         + 'Sunset: ' + sunset_time + '\n'


def cityDescription(weather_city):
    description = weather_city['weather'][0]['description'].title()

    humidity = weather_city['main']['humidity']

    #Wind speed measured in meters per second (mps)
    windSpeed = weather_city['wind']['speed']*2.23694

    #If deg is not given, return "No direction given"
    if 'wind' in weather_city: 
		wind = weather_city['wind']     
    if 'deg' in wind:
    	windDirection = weather_city['wind']['deg']
        windDirection = convert2cardinal.convert2cardinal(windDirection)
    else:
    	windDirection = "No direction given"
    #converts direction to NE, E, SE, S, SW, W, NW, or, N



    return 'Sky Description: ' + description + '\n' \
         + 'Humidity: ' + str(humidity) + '%' + '\n' \
         + 'Wind Speed: %.2f' % (windSpeed) + "mph" + '\n' \
         + 'Wind Direction: ' + str(windDirection) + '\n'


