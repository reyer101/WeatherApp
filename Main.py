from WeatherAPI import WeatherAPI
import WeatherConsts as Consts
import TempConverter
import TimeConverter
import convert2cardinal
import cityWeather
import zipWeather

def main():
    cityWeather.cityWeather()
    zipWeather.zipWeather()

if __name__ == "__main__":
    main()
