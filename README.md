#WeatherApp

@Authors:
    Megan Boyd (@boyd125)
    Elia Eiroa (@eliaeiroa)
    Sean Keelan (@keela101)
    Alec Reyerson (@reyer101)

Date last updated: 11/27/2016

Various applications and methods exist by which individuals retrieve information on the weather conditions of a given city or region. This information can be utilized for preparations in traveling to these areas, for event planning, or other purposes. Such preparations allow for greater living comfort and economic convenience.

OpenWeatherMap, Inc. provides tools which programmers can use to create applications or programs which provide information on weather conditions. The program, designed by this team using Python 2.7, utilizes OpenWeatherMap’s “Current weather data” API, gathering data in the JSON format and outputting information on a city’s weather conditions. Data is gathered from OpenWeatherMap’s API, and modified by functions found in the main Github repository to make information more readable for users.

The program will ask the user to input a city name, whose weather is checked in the API. Then, the program returns the data, collected in a Python dictionary, which contains dictionaries itself, and selects certain data for the user to read. This data will include the city’s name, country, current weather (e.g. clear sky, light rain, broken clouds, etc.), minimum, maximum and current temperatures in Fahrenheit and Celsius, wind speed and direction, humidity, times for sunrise and sunset, and other features. This program will offer users another resource from which they may retrieve their data on the weather.

Current functionality:
- Takes user input for city name and zip code.
  - Outputs current time, sunrise/sunset times, temperatures in Fahrenheit and
    Celsius, sky description, min/max temperatures of the day, humidity %,
    wind speed, and wind direction.

Compilation:
- The user must have the 'requests' library installed (at least in this current iteration)
- How to install 'requests':
  - If Pip is installed:
    - Enter the command: pip install requests in the Git Bash window
  - If Pip is NOT installed:
    - Enter: git clone git://github.com/kennethreitz/requests.git
    - Change current directory to requests
    - Type in: python setup.py install
  - Installation instructions for the 'requests' library can be found at:
    http://docs.python-requests.org/en/master/user/install/
- In Bash: python *.py

Contributions- 
Megan-
Elia-
Sean-
Alec-
