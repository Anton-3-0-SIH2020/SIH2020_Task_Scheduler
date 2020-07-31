import requests
from constants import BASE_URL
from configparser import ConfigParser

configure = ConfigParser()
configure.read('secret.ini')

API_KEY=configure.get('API_KEY', 'key')

def app(event=None, context=None):
    response = requests.get(f"{BASE_URL}nse?key={API_KEY}")
    json_resp = response.json()
    if json_resp.get('status', None):
        print('NSE DB Updated')
    else:
        print(json_resp.get('error','Something went wrong'))