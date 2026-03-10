# Justin DeGuzman
# justicd1@uci.edu
# 73239664

from OpenWeather import OpenWeather

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
