from unittest.mock import patch
from urllib.error import URLError, HTTPError
from weather import get_current_weather, UNAVAILABLE_MESSAGE


def test_get_current_weather():
    weather = get_current_weather("75001 Paris")
    assert weather == UNAVAILABLE_MESSAGE, 'Should return unavailable message because address format is invalid'


def test_get_current_weather_expected_behaviour(mocker):
    class ResponseMock:
        def __init__(self):
            pass

        def decode(self, code):
            return '{"count":1,"data":[{"app_temp":21.5,"aqi":35,"city_name":"Addison","clouds":0,"country_code":"US","datetime":"2023-05-07:12","dewpt":18.9,"dhi":68.61,"dni":610.08,"elev_angle":16.57,"ghi":235.57,"gust":12.34375,"h_angle":-77.1,"lat":32.96,"lon":-96.8385,"ob_time":"2023-05-07 12:51","pod":"d","precip":0,"pres":992,"rh":88,"slp":1014.32275,"snow":0,"solar_rad":235.6,"sources":["rtma"],"state_code":"TX","station":"KADS","sunrise":"11:33","sunset":"01:14","temp":21,"timezone":"America/Chicago","ts":1683463885,"uv":2.0449069,"vis":16,"weather":{"icon":"c01d","description":"Clear sky","code":800},"wind_cdir":"S","wind_cdir_full":"south","wind_dir":184,"wind_spd":2.1334975}]}'

        def read(self):
            return self

    mocker.patch("weather.urllib.request.urlopen", return_value=ResponseMock())
    weather = get_current_weather("Street 10, 75001 Paris, France")
    assert weather == 'Clear sky', 'Should return clear sky'


def test_get_current_weather_URLError():
    with patch("weather.urllib.request.urlopen", side_effect=URLError('mock', '500')):
        result = get_current_weather("Street 10, 75001 Paris, France")
        assert result == UNAVAILABLE_MESSAGE, 'Should return an unavailable message when URLError happened'
