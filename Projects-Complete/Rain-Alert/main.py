import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

# CONSTANTS ----
CITY = "Hong Kong"
LAT = 22.2855
LONG = 114.1577
CNT = 8

# weather API
load_dotenv()
apikey = os.environ.get("WEATHER_API_KEY")

# twilio API
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

# whatsapp number
whatsapp_num = os.environ.get("PHONE_NUMBER")

parameters = {
    "city name" : CITY,
    "app_id" : apikey
}

params_5 = {
    "lat" : LAT,
    "lon" : LONG,
    "cnt" : 8,
    "appid" : apikey
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=params_5)
response.raise_for_status()
weather_data = response.json()
will_rain = False

for i in range(0,CNT):
    weather_id = weather_data["list"][i]["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
    .create(
        body="It is going to rain today, bring an umbrella!",
        from_="whatsapp:+14155238886",
        to=f"whatsapp:{whatsapp_num}"
    )
    print(message.status)

# for hour_data in weather_data["list"]:
#     condition_code = hour_data["weather"][0]["id"]