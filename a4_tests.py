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
    