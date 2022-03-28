import requests
import json

def fuplode(s):
	r = requests.get(s)
	data = json.loads(r.text)
	return data