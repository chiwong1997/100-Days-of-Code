import requests
import os
from dotenv import load_dotenv

# ---- load env variables ----
load_dotenv()
SHEETY_BEARER_TOKEN = os.getenv("SHEETY_BEARER_TOKEN")
SHEETY_URL = "https://api.sheety.co/82fd2aebc26d853b9acc6a806c5e5510/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_url = SHEETY_URL
        self.sheety_bearer_token = SHEETY_BEARER_TOKEN
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=self.sheety_url, headers ={"Authorization": f"Bearer {self.sheety_bearer_token}"})
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    
    def update_destination_codes(self):
        """
        This method updates the IATA code for all cities in the Google Sheet. It loops through all the cities in the attribute 
        destination_data, and for each city, it makes a PUT request to update the IATA code for that city in the Google Sheet.
        """
        for city in self.destination_data:
            # note: Sheety expects your record to be nested in a singular root property named after your sheet. For example if your endpoint is named emails, nest your record in a property called email.
            # this caused me some confusion, as the root property should be the singular form of the sheet name (price not prices)- have not been able to find out why this is the case for Sheety
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            # put request from docs: https://api.sheety.co/phill/myWebsite/emails/2
            update_response = requests.put(url=f"{self.sheety_url}/{city['id']}", json=new_data, headers={"Authorization": f"Bearer {self.sheety_bearer_token}"})
            print(update_response.text)