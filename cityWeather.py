from WeatherAPI import WeatherAPI
import WeatherConsts as Consts
import TempConverter
import TimeConverter
import convert2cardinal


api_key = WeatherAPI(Consts.KEY)


#prints weaather by city
def cityWeather():

    print ('Enter the name of your city for current weather')
    city = raw_input('City: ')

    #city_api_key = api_key;
    weather_city = api_key.getWeatherCity(city)
    
    cityTimes(weather_city)
    cityTemps(weather_city)
    cityDescription(weather_city)



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
    
    print ('Current temperature in Fahrenheit: %.2f F' % tempF)
    print ('Current temperature in Celsius: %.2f C' % tempC)
    print ('Highs today are: %.2f F' % maxTempF)
    print ('Highs today are: %.2f C' % maxTempC)
    print ('Lows today are: %.2f F' % minTempF)
    print ('Lows today are: %.2f C' % minTempC)

#prints sunrise, sunset, and current time by city name
def cityTimes(weather_city):
    #Gets the current time and formats it like 02:00pm
    time = TimeConverter.current_time()
    
    #Gets sunset and sunrise times
    sunset_time = TimeConverter.time_convert(weather_city['sys']['sunset'])
    sunrise_time = TimeConverter.time_convert(weather_city['sys']['sunrise'])
    
    print ('\nCurrent time: ' + time)
    print ('Sunrise: ' + sunrise_time)
    print ('Sunset: ' + sunset_time)

def cityDescription(weather_city):
    description = weather_city['weather'][0]['description'].title()
    print ('Sky description: ' + description)
    
    humidity = weather_city['main']['humidity']
    print ('Humidity: ' + str (humidity) + '%')
    
    #Wind speed measured in meters per second (mps)
    windSpeed = weather_city['wind']['speed']*2.23694
    print ('Wind Speed: %.2f' % (windSpeed) + " mph")
    
    #If deg is not given, return "No direction given"
    if 'wind' in weather_city: 
	wind = weather_city['wind']     
    if 'deg' in wind:
    	windDirection = weather_city['wind']['deg']
    else:
    	windDirection = "No direction given"
    #converts direction to NE, E, SE, S, SW, W, NW, or, N
    print ('Wind Direction: ' + convert2cardinal.convert2cardinal(windDirection))



