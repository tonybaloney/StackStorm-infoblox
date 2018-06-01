import request

__all__ = [
    'GetTLSWeather',
]

class GetTLSWeather():
    def run(self, **kwargs):
import requests
        result = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Toulouse,fr&APPID=91a779c48c18e14f49b4d82ad2e4ff45')
        return result
