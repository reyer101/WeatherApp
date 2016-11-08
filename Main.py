from WeatherAPI import WeatherAPI
import WeatherConsts as Consts


def main():
    api = WeatherAPI(Consts.KEY)

    print 'Enter the name of your city for current weather'
    city = raw_input('City: ')

    weather = api.getWeather(city)

    print weather


if __name__ == "__main__":
    main()

