# Justin DeGuzman
# justicd1@uci.edu
# 73239664

from OpenWeather import OpenWeather
from LastFM import LastFM
from WebAPI import WebAPI
from unittest.mock import Mock
from ui import UI
import pytest
"""Pytest unit tests for Assignment 4 modules."""

"""OpenWeather class tests."""


def test_set_apikey_weather() -> None:
    """"OpenWeather stores API Key"""
    weather = OpenWeather()
    weather.set_apikey("testkey")

    assert weather.api_key == "testkey"


def test_transclude_weather_keyword() -> None:
    """OpenWeather should replace @weather."""
    weather = OpenWeather()
    weather.description = "clear sky"

    result = weather.transclude("Weather today is @weather")

    assert result == "Weather today is clear sky"


def test_transclude_weather_no_keyword() -> None:
    """OpenWeather should leave as is."""
    weather = OpenWeather()
    weather.description = "clear sky"

    result = weather.transclude("Hello!")

    assert result == "Hello!"


def test_transclude_weather_description_none() -> None:
    """Leave message unchanged if description not loaded."""
    weather = OpenWeather()
    weather.description = None

    result = weather.transclude("Weather today is @weather")

    assert result == "Weather today is @weather"


def test_transclude_weather_multiple_keywords() -> None:
    """Should replace all @weather occurrences."""
    weather = OpenWeather()
    weather.description = "sunny"

    result = weather.transclude("@weather and still @weather")

    assert result == "sunny and still sunny"


def test_init_custom_values() -> None:
    """Should store custom zipcode and ccdoe."""
    weather = OpenWeather("11111", "CA")

    assert weather.zipcode == "11111"
    assert weather.ccode == "CA"


"""LastFM class tests."""


def test_set_apikey_lastfm() -> None:
    """"LastFM stores API Key"""
    music = LastFM()
    music.set_apikey("testkey")

    assert music.api_key == "testkey"


def test_transclude_lastfm_keyword() -> None:
    """LastFM should replace @lastfm."""
    music = LastFM()
    music.artist = "Drake"

    result = music.transclude("Listening to @lastfm")

    assert result == "Listening to Drake"


def test_transclude_lastfm_no_keyword() -> None:
    """LastFM should leave as is."""
    music = LastFM()
    music.artist = "Drake"

    result = music.transclude("Hello!")

    assert result == "Hello!"


def test_transclude_lastfm_artist_none() -> None:
    """Leave message unchanged if artist is not loaded."""
    music = LastFM()
    music.artist = None

    result = music.transclude("Listening to @lastfm")

    assert result == "Listening to @lastfm"


def test_transclude_lastfm_multiple_keywords() -> None:
    """Replaces all @lastfm occurrences."""
    music = LastFM()
    music.artist = "Drake"

    result = music.transclude("@lastfm and @lastfm again")

    assert result == "Drake and Drake again"


"""WebAPI base class tests."""


def test_webapi() -> None:
    """Shouldn't be instantiated directly."""
    with pytest.raises(TypeError):
        WebAPI()


"""Unit tests for ui.py"""


def test_transclude_message_no_keywords():
    """Should return original message."""
    ui_obj = UI()
    message = "Hello!"

    result = ui_obj._transclude_message(message)

    assert result == "Hello!"


def test_process_line_routes_api():
    """Should route API command to configure API settings."""
    ui_obj = UI()
    ui_obj.current_profile = object()
    ui_obj.current_path = "/tmp/test.dsu"
    ui_obj._configure_api_settings = Mock()

    result = ui_obj._process_line("API")

    assert result is True
    ui_obj._configure_api_settings.assert_called_once_with()
