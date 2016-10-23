import requests
import json

def get_next_purchase_item():
	headers = {'username': 'giveitatry', 'password': 'Sh0wT!me', 'Content-Type': 'application/json'}
	data = {"accountNum": "100009"}

	r = requests.post('https://syf2020.syfwebservices.com/syf/nextMostLikelyPurchase', headers=headers, data = json.dumps(data))
	return r.text

if __name__ == "__main__":
	print(get_next_purchase_item())
