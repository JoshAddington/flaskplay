import json
import requests

URL = "http://bl.ocks.org/phil-pedruco/raw/6646844/830fab4f3a9cb28766c292c10fd99837bfcd1b80/nyc.json"

def get_boroughs():
        r = requests.get(URL)
        data = json.loads(r.text)
        return data
