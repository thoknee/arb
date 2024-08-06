import tkinter as tk

import requests
import json



import requests
import json
response_API = requests.get('https://api.the-odds-api.com/v4/sports/baseball_mlb/odds/?regions=us&oddsFormat=american&apiKey=f5d7b976a9cc1252a51661d07543cc54')

data = response_API.text
parse_json = json.loads(data)
print(parse_json)



