from WebAPI import WebAPI
from OpenWeather import OpenWeather
from LastFM import LastFM

WEATHER_KEY = "ad82f6236708c572a3190d5302dd9ac4"
LASTFM_KEY = "7fd54493df314cfe515993c2d3e09dde"


def test_api(message: str, apikey: str, webapi: WebAPI):
    webapi.set_apikey(apikey)
    webapi.load_data()
    result = webapi.transclude(message)
    print(result)


open_weather = OpenWeather()
lastfm = LastFM()

test_api("Testing the weather: @weather", WEATHER_KEY, open_weather)
test_api("Testing lastFM: @lastfm", LASTFM_KEY, lastfm)
