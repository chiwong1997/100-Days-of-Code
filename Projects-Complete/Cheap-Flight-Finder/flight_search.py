import requests
import os
from dotenv import load_dotenv

load_dotenv()
SERPAPI_FLIGHTSEARCH_ENDPOINT = "https://serpapi.com/search?engine=google_flights"

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.flightsearch_endpoint = SERPAPI_FLIGHTSEARCH_ENDPOINT
        self.serpapi_key = os.getenv("SERPAPI_KEY")

    def get_flight_data(self):
        # params = {
        #     "engine": "google_flights",
        #     "departure_id": "PEK",
        #     "arrival_id": "AUS",
        #     "outbound_date": "2026-03-17",
        #     "return_date": "2026-03-23",
        #     "currency": "USD",
        #     "hl": "en",
        #     "api_key": "secret_api_key"
        #     }
        pass

    def get_destination_code(self, city_name):
        code = "TESTING"
        return code
    