# Justin DeGuzman
# justicd1@uci.edu
# 72329664

# openweather.py

import urllib
import json
from urllib import request, error


class OpenWeather:
    def __init__(self, zipcode: str, ccode: str) -> None:
        self.zipcode = zipcode
        self.ccode = ccode

        # initializing components from OpenWeather API
        self.temperature = None
        self.high_temperature = None
        self.low_temperature = None
        self.longitude = None
        self.latitude = None
        self.description = None
        self.humidity = None
        self.city = None
        self.sunset = None

    # helper function obtained from Assignment4 Part1
    def _download_url(self, url_to_download: str) -> dict:
        response = None
        r_obj = None

        try:
            response = urllib.request.urlopen(url_to_download)
            json_results = response.read()
            r_obj = json.loads(json_results)

        except urllib.error.HTTPError as e:
            print('Failed to download contents of URL')
            print('Status code: {}'.format(e.code))

        finally:
            if response is not None:
                response.close()

        return r_obj

    # defines API key for the class
    def set_apikey(self, apikey: str) -> None:
        self.api_key = apikey
        pass

    # obtains components from OpenWeather while checking for various errors
    def load_data(self) -> None:
        try:
            url_to_download = (
                f"http://api.openweathermap.org/data/2.5/weather"
                f"?zip={self.zipcode},{self.ccode}&appid={self.api_key}"
            )

            weather_obj = self._download_url(url_to_download)

            if weather_obj is None:
                raise Exception("OpenWeather API returned an HTTP error.")

            self.temperature = weather_obj["main"]["temp"]
            self.high_temperature = weather_obj["main"]["temp_max"]
            self.low_temperature = weather_obj["main"]["temp_min"]
            self.longitude = weather_obj["coord"]["lon"]
            self.latitude = weather_obj["coord"]["lat"]
            self.description = weather_obj["weather"][0]["description"]
            self.humidity = weather_obj["main"]["humidity"]
            self.city = weather_obj["name"]
            self.sunset = weather_obj["sys"]["sunset"]

        except urllib.error.URLError as e:
            raise Exception("Lost local connection from Internet.") from e

        except (KeyError, TypeError, json.JSONDecodeError) as e:
            raise Exception("Invalid data format from OpenWeather API.") from e

    def transclude(self, message: str) -> str:
        if "@weather" not in message:
            return message

        if self.description is None:
            return message

        return message.replace("@weather", self.description)


open_weather = OpenWeather("92697", "US")
open_weather.set_apikey("ad82f6236708c572a3190d5302dd9ac4")
open_weather.load_data()
msg = "Today's weather is @weather."
print(open_weather.transclude(msg))
