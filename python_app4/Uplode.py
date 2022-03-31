import requests
import json

def fuplode(s):
	try:
		r = requests.get(s)
		print(r.content)
		data = json.loads(r.text)
		return data
	except requests.exceptions.MissingSchema:
		return None