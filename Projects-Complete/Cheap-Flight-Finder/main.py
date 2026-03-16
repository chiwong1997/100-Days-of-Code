import requests
import os
from dotenv import load_dotenv

# ---- load env variables ----
load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

SHEETY_BEARER_TOKEN = os.getenv("SHEETY_BEARER_TOKEN")
SHEETY_URL = "https://api.sheety.co/82fd2aebc26d853b9acc6a806c5e5510/flightDeals/prices"

# ---- Sheety API ----
response = requests.get(url=SHEETY_URL, headers={"Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"})
print(response.text)