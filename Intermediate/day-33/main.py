import requests
import datetime as dt

# ----iss API----

# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# # print(response)
# # print(response.status_code)
# response.raise_for_status()
# data = response.json()
# print(data)
# # access the data as normal 
# print(data["iss_position"]["longitude"])
# print(data["timestamp"])

# iss_position = (data["iss_position"]["longitude"], data["iss_position"]["latitude"])
# print(iss_position)

# ---- sunset API ----

MY_LAT = 22.2792968
MY_LONG = 114.1628907

parameters = {"lat": MY_LAT, 
              "lng": MY_LONG,
              "formatted": 0
              }

response = requests.get(url='https://api.sunrise-sunset.org/json', params = parameters)
# in the browser, we can write the parameters like this to access the information : 
# https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&formatted=0
data = response.json()
print(data)
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
sunrise_hour = sunrise.split("T")[1].split(":")[0]
print(sunrise_hour)

now = dt.datetime.now()
print(now.hour)