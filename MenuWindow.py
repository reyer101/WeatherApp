import cityWeather
import cityForecast
import zipWeather
from Tkinter import *
from ScrolledText import *

# Initialize program components:
def init():
    # Create and set up the main window:
    global window
    window = Tk()
    window.title('WeatherApp')
    window.geometry("250x350")
    createWidgets()
    positionWidgets()
    configureWidgets()
    # Display the window:
    window.mainloop()

# Create widget objects:
def createWidgets():
    global column; column = Frame(window)
    global cityWeatherButton; cityWeatherButton = Button(window)
    global zipWeatherButton; zipWeatherButton = Button(window)
    global cityForecastButton; cityForecastButton = Button(window)


# Position the widgets in the window:
def positionWidgets():

    column.place(relx=.5, rely=.5, anchor=CENTER)

    cityWeatherButton.pack(in_=column, side=BOTTOM, pady=50)
    zipWeatherButton.pack(in_=column, side=TOP, pady=50)
    cityForecastButton.pack(in_=column, side=BOTTOM)



# Configure the widgets:
def configureWidgets():
    window.configure(background="light sky blue")
    column.configure(background="light sky blue")

    cityWeatherButton.configure(text="WEATHER BY CITY", height=2, width=20, command=cityWeatherAction)
    zipWeatherButton.configure(text="WEATHER BY ZIP", height=2, width=20, command=zipWeatherAction)
    cityForecastButton.configure(text="FORECAST BY CITY", height=2, width=20, command=cityForecastAction)


def cityWeatherAction():       #Triggered when "Weather by City" button is pressed
    cwWindow = Toplevel()
    cwWindow.geometry("400x400")
    cwWindow.title('CityWeather')
    cwWindow.configure(background="light sky blue")

    global weatherDisplay
    global cityEntry

    innerFrame = Frame(cwWindow)
    outterFrame = Frame(cwWindow)



    cityLabel = Label(cwWindow)
    cityEntry = Entry(cwWindow)
    weatherButton = Button(cwWindow)
    weatherDisplay = ScrolledText(cwWindow)

    cityLabel.pack(in_=innerFrame, side=LEFT)  #Packs inner Frame
    cityEntry.pack(in_=innerFrame, side=RIGHT)


    innerFrame.pack(in_=outterFrame, side=TOP)       #Packs outter Frame
    weatherDisplay.pack(in_=outterFrame, side=BOTTOM)
    weatherButton.pack(in_=outterFrame, side=BOTTOM)



    outterFrame.grid(column=0, row=0, padx=3, pady=3)   #Places outter Frame


    outterFrame.configure(background="light sky blue")
    innerFrame.configure(pady=4, background="light sky blue")
    weatherButton.configure(width=10, height=1, text="GET WEATHER", command=getCityWeatherAction)     #Configures widgets
    cityLabel.configure(width=7, height=1, text="City", relief=SUNKEN)
    weatherDisplay.configure(width=45, height=17, pady=3, padx=3)


def zipWeatherAction():
    zwWindow = Toplevel()
    zwWindow.geometry("400x400")
    zwWindow.title('ZipWeather')
    zwWindow.configure(background="light sky blue")

    global zipWeatherDisplay
    global zipEntry

    innerFrame = Frame(zwWindow)
    outterFrame = Frame(zwWindow)

    zipLabel = Label(zwWindow)
    zipEntry = Entry(zwWindow)
    weatherButton = Button(zwWindow)
    zipWeatherDisplay = ScrolledText(zwWindow)

    zipLabel.pack(in_=innerFrame, side=LEFT)  # Packs inner Frame
    zipEntry.pack(in_=innerFrame, side=RIGHT)

    innerFrame.pack(in_=outterFrame, side=TOP)  # Packs outter Frame
    zipWeatherDisplay.pack(in_=outterFrame, side=BOTTOM)
    weatherButton.pack(in_=outterFrame, side=BOTTOM)

    outterFrame.grid(column=0, row=0, padx=3, pady=3)  # Places outter Frame

    outterFrame.configure(background="light sky blue")
    innerFrame.configure(pady=4, background="light sky blue")
    weatherButton.configure(width=10, height=1, text="GET WEATHER", command=getZipWeatherAction)  # Configures widgets
    zipLabel.configure(width=7, height=1, text="Zip Code", relief=SUNKEN)
    zipWeatherDisplay.configure(width=45, height=17, pady=3, padx=3)

def cityForecastAction():
    cfWindow = Toplevel()
    cfWindow.geometry("400x400")
    cfWindow.title('CityForecast')
    cfWindow.configure(background="light sky blue")

    global forecastDisplay
    global cityFEntry

    innerFrame = Frame(cfWindow)
    outterFrame = Frame(cfWindow)

    cityLabel = Label(cfWindow)
    cityFEntry = Entry(cfWindow)
    forecastButton = Button(cfWindow)
    forecastDisplay = ScrolledText(cfWindow)

    cityLabel.pack(in_=innerFrame, side=LEFT)  # Packs inner Frame
    cityFEntry.pack(in_=innerFrame, side=RIGHT)

    innerFrame.pack(in_=outterFrame, side=TOP)  # Packs outter Frame
    forecastDisplay.pack(in_=outterFrame, side=BOTTOM)
    forecastButton.pack(in_=outterFrame, side=BOTTOM)

    outterFrame.grid(column=0, row=0, padx=3, pady=3)  # Places outter Frame

    outterFrame.configure(background="light sky blue")
    innerFrame.configure(pady=4, background="light sky blue")
    forecastButton.configure(width=11, height=1, text="GET FORECAST", command=getCityForecastAction)  # Configures widgets
    cityLabel.configure(width=7, height=1, text="City", relief=SUNKEN)
    forecastDisplay.configure(width=45, height=17, pady=3, padx=3)


def getCityWeatherAction():
    city = str(cityEntry.get())   #Sets the city as the string value of the cityEntry box
    weather = cityWeather.cityWeather(city)

    weatherDisplay.insert(END, weather)

def getZipWeatherAction():
    zip = str(zipEntry.get())     #Sets the zip as the string value of the zipEntry box
    weather = zipWeather.zipWeather(zip)

    zipWeatherDisplay.insert(END, weather)  #Sets the city as the string value of the cityFEntry box

def getCityForecastAction():
    city = str(cityFEntry.get())
    forecast = cityForecast.getCityForecast(city)

    forecastDisplay.insert(END, forecast)



def fpToString(value, decimalPositions):
    string = str(round(value, decimalPositions));
    periodPosition = string.find('.');
    if (periodPosition >= 0):
        string = string[0: periodPosition + decimalPositions + 1];
    return string;
    # Example: fpToString(value = 3.14159, decimalPositions = 2) returns '3.14'.

# Create the GUI and show it:

