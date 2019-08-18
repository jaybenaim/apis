import requests 
import json 

response = requests.get('https://represent.opennorth.ca/boundaries/?sets=ottawa-wards')

body = json.loads(response.content) 
for name in body['objects']: 
    print(name['name']) 