README file for WeatherApp

@Authors:
    Megan Boyd (@boyd125)
    Elia Eiroa (@eliaeiroa)
    Sean Keelan (@keela101)
    Alec Reyerson (@reyer101)

Date last updated: 11/26/2016

Various applications and methods exist by which individuals retrieve information on the weather conditions of a given city or region. This information can be utilized for preparations in traveling to these areas, for event planning, or other purposes. Such preparations allow for greater living comfort and economic convenience.

OpenWeatherMap, Inc. provides tools which programmers can use to create applications or programs which provide information on weather conditions. The program, designed by this team using Python 2.7, utilizes OpenWeatherMap’s “Current weather data” API, gathering data in the JSON format and outputting information on a city’s weather conditions. Data is gathered from OpenWeatherMap’s API, and modified by functions found in the main Github repository to make information more readable for users.

The program will ask the user to input a city name, whose weather is checked in the API. Then, the program returns the data, collected in a Python dictionary, which contains dictionaries itself, and selects certain data for the user to read. This data will include the city’s name, country, current weather (e.g. clear sky, light rain, broken clouds, etc.), minimum, maximum and current temperatures in Fahrenheit and Celsius, wind speed and direction, humidity, times for sunrise and sunset, and other features. This program will offer users another resource from which they may retrieve their data on the weather.
