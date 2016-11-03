import requests
import WeatherConsts as Consts


class WeatherAPI(object):
    def __init__(self, key, _city, _country = 'US', _zip = 0 ):
        self.api_key = key
        self.city = _city

    def _request(self, api_url):
        response = requests.get(Consts.URL['base'].format(
            url=api_url
        ))

        return response.json()

    def getWeather(self, city):

        response = self._request(Consts.URL['current'].format(
            city=city,
            key=Consts.KEY
        ))

        return response

