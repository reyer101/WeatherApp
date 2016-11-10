#TempConverter.py
#Description: Utility class to convert temperatures to different degrees.
#Functionality for conversions from Kelvin (K) to Fahrenheit (F),
#Kelvin to Celsius (C), F to C, C to F, F to K, and C to K
#Equations:
# Kelvin to Fahrenheit: F = (K - 273.15) * (9/5) + 32
# Kelvin to Celsius: C = K - 273.15
# Fahrenheit to Celsius: C = (F - 32) * (5/9)
# Celsius to Fahrenheit: F = [C * (9/5)] + 32
# Fahrenheit to Kelvin: K = (F - 32) * 5/9 + 273.15
# Celsius to Kelvin: K = C + 273.15
#Author: Sean Keelan

def convertKtoF(kelvin):
    f = (kelvin - 273.15) * 9/5 + 32
    return f

def convertKtoC(kelvin):
    c = kelvin - 273.15
    return c

def convertFtoC(fahrenheit):
    c = (fahrenheit - 32) * 5/9
    return c

def convertCtoF(celsius):
    f = celsius * 9/5 + 32
    return f

def convertFtoK(fahrenheit):
    k = (fahrenheit - 32) * 5/9 + 273.15
    return k

def convertCtoK(celsius):
    k = celsius + 273.15
    return k
