# Justin DeGuzman
# justicd1@uci.edu
# 72329664

# webapi.py

from abc import ABC, abstractmethod
import urllib
import json
from urllib import request, error


class WebAPI(ABC):
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
        pass

    @abstractmethod
    def load_data(self) -> None:
        pass

    @abstractmethod
    def transclude(self, message: str) -> str:
        pass
