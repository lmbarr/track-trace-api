from unittest.mock import patch
from main import get_weather
import pytest

from weather import UNAVAILABLE_MESSAGE


def test_get_weather_from_cache(mocker):
    m = mocker.patch("main.get_cache_value", return_value='Cloudy')
    result = get_weather('TN12345678', 'DHL', 'Street 10, 75001 Paris, France')
    m.assert_called_once_with('TN12345678:DHL')
    assert result == 'Cloudy', 'Should used cached value'


def test_get_weather_from_api(mocker):
    mocker.patch("main.get_cache_value", return_value=None)
    mocker.patch("main.get_current_weather", return_value='Cloudy')
    set_cache_value_mocked = mocker.patch("main.set_cache_value", return_value=None)
    result = get_weather('TN12345678', 'DHL', 'Street 10, 75001 Paris, France')
    set_cache_value_mocked.assert_called_once_with('TN12345678:DHL', 'Cloudy')
    assert result == 'Cloudy', 'Should set value in cache'


def test_get_weather_exception():
    with patch('main.get_current_weather', side_effect=Exception('mocked error')):
        result = get_weather('TN12345678', 'DHL', 'Street 10, 75001 Paris, France')
        assert result == UNAVAILABLE_MESSAGE, 'Should return an unavailable message'
