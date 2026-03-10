import datetime as dt
import requests
from dotenv import load_dotenv
import os

# ---- load env variables ----
load_dotenv()
NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY")
