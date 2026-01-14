import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json')
# print(response)
# print(response.status_code)
response.raise_for_status()
data = response.json()
print(data)
# access the data as normal 
print(data["iss_position"]["longitude"])
print(data["timestamp"])

iss_position = (data["iss_position"]["longitude"], data["iss_position"]["latitude"])
print(iss_position)