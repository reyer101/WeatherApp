#WeatherApp

@Authors:
    Megan Boyd (@boyd125)
    Elia Eiroa (@eliaeiroa)
    Sean Keelan (@keela101)
    Alec Reyerson (@reyer101)

Date last updated: 11/27/2016

Various applications and methods exist by which individuals retrieve information on the weather conditions of a given city or region. This information can be utilized for preparations in traveling to these areas, for event planning, or other purposes. Such preparations allow for greater living comfort and economic convenience.

OpenWeatherMap, Inc. provides tools which programmers can use to create applications or programs which provide information on weather conditions. The program, designed by this team using Python 2.7, utilizes OpenWeatherMap’s “Current weather data” API, gathering data in the JSON format and outputting information on a city’s weather conditions. Data is gathered from OpenWeatherMap’s API, and modified by functions found in the main Github repository to make information more readable for users.

The program will ask the user to input a city name, whose weather is checked in the API. Then, the program returns the data, collected in a Python dictionary, which contains dictionaries itself, and selects certain data for the user to read. This data will include the city’s name, country, current weather (e.g. clear sky, light rain, broken clouds, etc.), minimum, maximum and current temperatures in Fahrenheit and Celsius, wind speed and direction, humidity, times for sunrise and sunset, and other features. In addition there will be a five day forecast option that will allow the user to view a brief estimate of the future weather in the desired location.  This program will offer users another resource from which they may retrieve their data on the weather.

Current functionality:
- Takes user input for city name and zip code.
  - Outputs current time, sunrise/sunset times, temperatures in Fahrenheit and
    Celsius, sky description, min/max temperatures of the day, humidity %,
    wind speed, and wind direction.

Compilation & Installations:
- The user must have the 'requests' library installed (at least in this current iteration)
- How to install 'requests':
  - If Pip is installed:
    - Enter the command: pip install requests in the Git Bash window
    - OR Enter: python.exe -m pip install requests
  - How to upgrade Pip if not currently updated:
    - On Linux or Mac, enter: pip install -U pip
    - On Windows, enter: python -m pip install -U pip
  - Instructions to install Pip can be found at:
      http://docs.python-guide.org/en/latest/starting/installation/
  - If Pip is NOT installed:
    - Go to your home directory
    - Enter the command: git clone git://github.com/kennethreitz/requests.git
    - Change current directory to requests
    - Enter the command: python setup.py install
  - Installation instructions for the 'requests' library can be found at:
    http://docs.python-requests.org/en/master/user/install/
  - Installing the setuptools Python module if setuptools is NOT installed:
    - Instructions can be found on the Python Software Foundation's
      setuptools-29.0.1 : Python Package Index at the web address in the following
      instructions.
    - Go to: https://pypi.python.org/pypi/setuptools#downloads and download
      the following files found at the bottom of the page:
          setuptools-29.0.1-py2.py3-none-any.whl (md5)
          setuptools-29.0.1.tar.gz (md5)
          setuptools-29.0.1.zip (md5)
      - Included in these downloads is a file called ez_setup.py. To install the
        setuptools module:
        - Windows
          - In the PowerShell tool, download ez_setup.py using the following command:
                (Invoke-WebRequest https://bootstrap.pypa.io/ez_setup.py).Content | python -
          - Run ez_setup.py with the command: python ez_setup.py
        - Unix (Linux and Mac OSX)
          - In your Unix terminal, download ez_setup.py using the following command:
                wget https://bootstrap.pypa.io/ez_setup.py -O - | python
            - If you need to invoke the command using superuser privileges
              (i.e. if you are restrited from using the previous command), enter:
                  wget https://bootstrap.pypa.io/ez_setup.py -O - | sudo python
            - Alternatively, if you have curl, you can instead enter thir command:
                  curl https://bootstrap.pypa.io/ez_setup.py -o - | python
          - Once ez_setup.py is downloaded, run ez_setup.py with the command:
              python ez_setup.py
          - If you are using an older version of Unix, the wget command may output
            some error. If this is the case, enter:
                wget --no-check-certificate https://bootstrap.pypa.io/ez_setup.py
                python ez_setup.py --insecure

- In Bash: python *.py

Contributions-
Megan-
Elia-
Sean-
Alec-
