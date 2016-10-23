import requests
import json
import random

def get_next_purchase_item():
	headers = {'username': 'giveitatry', 'password': 'Sh0wT!me', 'Content-Type': 'application/json'}
	randacct = random.randrange(100000, 105000)
	data = {"accountNum": str(randacct)}
	r = requests.post('https://syf2020.syfwebservices.com/syf/nextMostLikelyPurchase', headers=headers, data = json.dumps(data))
	resp = r.json()
	categories = resp['categories']
	maxcat = 0
	maxelem = {}
	for i in range(categories):
		if categories[i]['probability'] > maxcat:
			maxcat = categories[i]['probability']
			maxelem = categories[i]
	return maxelem

if __name__ == "__main__":
	print(get_next_purchase_item())
