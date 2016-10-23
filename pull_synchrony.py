import requests
import json
import random

headers = {'username': 'giveitatry', 'password': 'Sh0wT!me', 'Content-Type': 'application/json'}
all_codes = {}
for x in range(100000, 105000):
    randacct = str(x)
    data = {"accountNum": str(randacct)}
    r = requests.post('https://syf2020.syfwebservices.com/syf/nextMostLikelyPurchase', headers=headers, data = json.dumps(data))
    resp = r.json()
    categories = resp['categories']
    maxcat = 0
    maxelem = {}
    for i in range(len(categories)):
    	if categories[i]['probability'] > maxcat:
    		maxcat = categories[i]['probability']
    		maxelem = categories[i]
    all_codes[x] = maxelem
print(json.dumps(all_codes))
