import requests
from st2common.runners.base_action import Action

__all__ = [
    'GetWeather',
]

class GetWeather(Action):
    # def __init__(self):
    #     pass

    def run(self, city, **kwargs):
        result = requests.get('https://api.openweathermap.org/data/2.5/weather?q={}&APPID=91a779c48c18e14f49b4d82ad2e4ff45'.format('city'))
        return result.json()
