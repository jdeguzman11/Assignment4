# Justin DeGuzman
# justicd1@uci.edu
# 72329664

# lastfm.py

# test key: 7fd54493df314cfe515993c2d3e09dde
"""LastFM API class for loading music data and transcluding @lastfm."""

import urllib
import json
from WebAPI import WebAPI


class LastFM(WebAPI):
    """Represents a LastFM web API client."""

    def __init__(self):
        self.api_key = None
        self.artist = None

    def load_data(self) -> None:
        try:
            url_to_download = (
                f"http://ws.audioscrobbler.com/2.0/?method="
                f"chart.gettopartists&api_key={self.api_key}&format=json"
            )

            artist_obj = self._download_url(url_to_download)

            if artist_obj is None:
                raise RuntimeError("LastFM API returned an HTTP error.")

            top_artist = artist_obj["artists"]["artist"][0]
            self.artist = top_artist["name"]

        except urllib.error.URLError as e:
            raise RuntimeError("Lost local connection from Internet.") from e

        except (KeyError, IndexError, TypeError, json.JSONDecodeError) as e:
            raise RuntimeError("Invalid data format from LastFM API.") from e

    def transclude(self, message: str) -> str:
        if "@lastfm" not in message:
            return message

        if self.artist is None:
            return message

        return message.replace("@lastfm", self.artist)
