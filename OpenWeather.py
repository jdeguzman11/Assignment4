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

        self.temperature = None
        self.high_temperature = None
        self.low_temperature = None
        self.longitude = None
        self.latitude = None
        self.description = None
        self.humidity = None
        self.city = None
        self.sunset = None

    def set_apikey(self, apikey: str) -> None:
        self.api_key = apikey
        pass

    def load_data(self) -> None:
        pass

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
