import json

def get_api_key(api):
	key = ''
	with open('apikeys.json', 'r') as f:
		keys = json.load(f)
		key = keys[api]
	return key