
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
    zipWeatherButton.configure(text="WEATHER BY ZIP", height=2, width=20)
    cityForecastButton.configure(text="FORECAST BY CITY", height=2, width=20)


def cityWeatherAction():
    cwWindow = Toplevel()
    cwWindow.geometry("200x300")







def fpToString(value, decimalPositions):
    string = str(round(value, decimalPositions));
    periodPosition = string.find('.');
    if (periodPosition >= 0):
        string = string[0: periodPosition + decimalPositions + 1];
    return string;
    # Example: fpToString(value = 3.14159, decimalPositions = 2) returns '3.14'.

# Create the GUI and show it:

