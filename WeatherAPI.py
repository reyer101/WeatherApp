import requests
import WeatherConsts as Consts


class WeatherAPI(object):
    def __init__(self, key):
        self.api_key = key


    def _request(self, api_url):
        response = requests.get(Consts.URL['base'].format(
            url=api_url
        ))

        return response.json()

    def getWeatherCity(self, city):

        response = self._request(Consts.URL['current'].format(
            city=city,
            key=Consts.KEY
        ))

        return response

    def getWeatherZip(self, zip):

        response = self._request(Consts.URL['current_zip'].format(
            zip=zip,
            country='us',
            key=Consts.KEY
        ))

        return response

    def getForecastCity(self, city):

        response = self._request(Consts.URL['forecast'].format(
            city=city,
            country='us',
            key=Consts.KEY
        ))

