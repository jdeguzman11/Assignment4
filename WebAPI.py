# Justin DeGuzman
# justicd1@uci.edu
# 72329664

# webapi.py
"""Abstract base class for web API clients used in the DSU application."""

from abc import ABC, abstractmethod
import urllib
import json


class WebAPI(ABC):
    """Parent class OpenWeather and LastFM inherit from."""
    
    def _download_url(self, url: str) -> dict:
        response = None
        r_obj = None

        try:
            response = urllib.request.urlopen(url)
            json_results = response.read()
            r_obj = json.loads(json_results)

        except urllib.error.HTTPError as e:
            print('Failed to download contents of URL')
            print('Status code: {}'.format(e.code))

        finally:
            if response is not None:
                response.close()

        return r_obj

    def set_apikey(self, apikey: str) -> None:
        self.api_key = apikey

    @abstractmethod
    def load_data(self) -> None:
        pass

    @abstractmethod
    def transclude(self, message: str) -> str:
        pass
