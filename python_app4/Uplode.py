import requests
import json

def fuplode(s):
	try:
		r = requests.get(s)
		data = json.loads(r.text)
		return data
	except (requests.exceptions.MissingSchema, json.decoder.JSONDecodeError):
		return None