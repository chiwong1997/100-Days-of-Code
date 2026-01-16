import requests
import datetime as dt
import smtplib
import time

# ----constants----
MY_LAT = 22.2792968
MY_LONG = 114.1628907
GMAIL_SMTP = "smtp.gmail.com"
PORT = 587
MY_EMAIL = "100daysofcodeproject@gmail.com"
MY_PASSWORD = "flhitjcbrwhfybmx"

# ----functions----

def is_iss_overhead():
    iss_response = requests.get(url='http://api.open-notify.org/iss-now.json')
    iss_response.raise_for_status()
    iss_data = iss_response.json()
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    return False

def is_night():
    parameters = {"lat": MY_LAT, 
                "lng": MY_LONG,
                "formatted": 0
                }

    response = requests.get(url='https://api.sunrise-sunset.org/json', params = parameters)
    data = response.json()
    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']
    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour = int(sunset.split("T")[1].split(":")[0])

    now = dt.datetime.now().hour

    if now >= sunset or now <=sunrise:
        return True
    return False

#----code----
# this following line of code will make the program run every 2 minutes forever
# while True: 
#     time.sleep(120)

if is_iss_overhead() == True and is_night() == True:
    print("Email will be sent")
    with smtplib.SMTP(GMAIL_SMTP,port=PORT) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="randomemail.gmail.com",
                            msg="Subject:Look for the ISS!\n\nThere is a chance to see the ISS tonight!"
                            )