import requests
res = requests.get('http://10.12.200.18:92/simulation/hw/trucksnap/get')
print(res.text)