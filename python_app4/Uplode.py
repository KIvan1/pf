import requests
import json

def fuplode():
	r = requests.get("http://kappa.cs.petrsu.ru/~dimitrov/info_1/test.json")
	data = json.loads(r.text)
	return data