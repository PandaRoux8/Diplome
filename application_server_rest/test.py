import requests
import json

url = "http://127.0.0.1:8000"
data = {'username': "Chat", 'password': "lapin"}
r = requests.post(url+"/authenticate", json=json.dumps(data))
print(r, r.status_code)
r = requests.post(url+"/authenticate-user", json=json.dumps(data))
print(r, r.status_code)
