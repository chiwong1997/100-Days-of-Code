import datetime as dt
import requests
from dotenv import load_dotenv
import os

# ---- load env variables ----
load_dotenv()
NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY")
SHEETY_BEARER_TOKEN = os.getenv("SHEETY_BEARER_TOKEN")

# ---- constants ----
BASE_URL = "https://app.100daysofpython.dev"
HEADERS = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY
}
SHEETY_URL = "https://api.sheety.co/82fd2aebc26d853b9acc6a806c5e5510/workoutTracker/workouts"

# Exercise API - calculate and get the calories burned for a given exercise
# -----------------------------------------------
exercise_endpoint = f"{BASE_URL}/v1/nutrition/natural/exercise"
exercise_text = input("What exercise did you do today? ")
exercise_params = {
    "query": exercise_text,
    "weight_kg": 88,
    "height_cm": 186,
    "age": 28,
    "gender": "male"
}

exercise_api_post_response = requests.post(url=exercise_endpoint, json=exercise_params, headers=HEADERS)
print(exercise_api_post_response.text)

# Sheety API - workout data to Google Sheet
# ----------------------------------------------
# response = requests.get(url=SHEETY_URL)
# print(response.text)

# to_delete = input("Which workout entry do you want to delete?: ")
# delete_row_endpoint = f"{SHEETY_URL}/{to_delete}"
# delete_response = requests.delete(url=delete_row_endpoint)
# print(delete_response.text)

sheety_params = {
    "workout": {
        "date": dt.datetime.now().strftime("%d/%m/%Y"),
        "time": dt.datetime.now().strftime("%H:%M:%S"),
        "exercise": exercise_api_post_response.json()["exercises"][0]["user_input"].title(),
        "duration": exercise_api_post_response.json()["exercises"][0]["duration_min"],
        "calories": exercise_api_post_response.json()["exercises"][0]["nf_calories"]
    }
}

bearer_headers = {
    "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
}

response = requests.post(url=SHEETY_URL, json=sheety_params, headers=bearer_headers)
print(response.text)