import requests
import json

def get_data(url):
	r = requests.get(url)
	response = []
	
	if r.status_code == 200:
		response = r.json()

	return response

def get_highest_volume(response):
	highest_volume = 0
	
	for item in response:
		highest_volume = max(highest_volume,float(item["24h_volume_usd"]))

	return highest_volume

url = "https://api.coinmarketcap.com/v1/ticker/"
response = get_data(url)
highest_volume = 0

highest_volume = get_highest_volume(response)	

print (highest_volume)	