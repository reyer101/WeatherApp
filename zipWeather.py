from WeatherAPI import WeatherAPI
import WeatherConsts as Consts

import TempConverter
import TimeConverter
import convert2cardinal

api_key = WeatherAPI(Consts.KEY)

#prints weather by zip code
def zipWeather():

    print ('\nEnter the zip code of another city')
    zip_code = raw_input('Zip code: ')

    #zip_api_key = api_key;
    weather_zip = api_key.getWeatherZip(zip_code)
    
    zipTimes(weather_zip)
    zipTemps(weather_zip)
    zipDescription(weather_zip)

#prints sunrise, sunset, and current time by zip-code

def zipTimes(weather_zip):
    
    #Gets the current time and formats it like 02:00pm
    time = TimeConverter.current_time()
    
    #Gets sunset and sunrise times
    sunset_time = TimeConverter.time_convert(weather_zip['sys']['sunset'])
    sunrise_time = TimeConverter.time_convert(weather_zip['sys']['sunrise'])
    
    print ('\nCurrent time: ' + time)
    print ('Sunrise: ' + sunrise_time)
    print ('Sunset: ' + sunset_time)

def zipTemps(weather_zip):
    temperature = weather_zip['main']['temp']
    tempF = TempConverter.convertKtoF(temperature)
    tempC = TempConverter.convertKtoC(temperature)
    
    minTemperature = weather_zip['main']['temp_min']
    minTempF = TempConverter.convertKtoF(minTemperature)
    minTempC = TempConverter.convertKtoC(minTemperature)
    
    maxTemperature = weather_zip['main']['temp_max']
    maxTempF = TempConverter.convertKtoF(maxTemperature)
    maxTempC = TempConverter.convertKtoC(maxTemperature)
    
    print ('Current temperature in Fahrenheit: %.2f F' % tempF)
    print ('Current temperature in Celsius: %.2f C' % tempC)
    print ('Highs today are: %.2f F' % maxTempF)
    print ('Highs today are: %.2f C' % maxTempC)
    print ('Lows today are: %.2f F' % minTempF)
    print ('Lows today are: %.2f C' % minTempC)

def zipDescription(weather_zip):
    description = weather_zip['weather'][0]['description'].title()
    print ('Sky description: ' + description)
    
    humidity = weather_zip['main']['humidity']
    print ('Humidity: ' + str (humidity) + '%')
    
    #Wind speed measured in meters per second (mps)
    windSpeed = weather_zip['wind']['speed']*2.23694
    print ('Wind Speed: %.2f' % (windSpeed) + " mph")
    
    #If deg is not given, does not work
    if 'wind' in weather_zip: 
	wind = weather_zip['wind']     
    if 'deg' in wind:
    	windDirection = weather_zip['wind']['deg']
    else:
    	windDirection = "No direction given"
    #converts direction to NE, E, SE, S, SW, W, NW, or, N
    print ('Wind Direction: ' + convert2cardinal.convert2cardinal(windDirection))

    
