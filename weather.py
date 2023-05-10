import os
import urllib.request
import json
from urllib.error import URLError, HTTPError

UNAVAILABLE_MESSAGE = 'No weather data available'


def address_to_city(address):
    return address.split(', ')[1].split(' ')[1]


def get_current_weather(address):
    try:
        postal_code = address_to_postal_code(address)
        city = address_to_city(address)
    except:
        print('Format error')
        return UNAVAILABLE_MESSAGE

    # TODO handle api secret in a approprieate way

    api_key = os.getenv('WEATHER_API_KEY')

    url = 'https://api.weatherbit.io/v2.0/current?postal_code={}&key={}&city={}'.format(postal_code, api_key, city)

    try:
        response = urllib.request.urlopen(url)
        data = response.read().decode('utf-8')
    except HTTPError as e:
        print('Error code: ', e.code)
        return UNAVAILABLE_MESSAGE
    except URLError as e:
        print('Reason: ', e.reason)
        return UNAVAILABLE_MESSAGE

    return json.loads(data)['data'][0]['weather']['description']


def address_to_postal_code(address):
    return address.split(', ')[1].split(' ')[0]
