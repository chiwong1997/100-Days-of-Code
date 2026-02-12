import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv
import datetime as dt

# ----constants----
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# load environment variables
load_dotenv()
alpha_vantage_api_key = os.environ.get("ALPHA_VANTAGE_API_KEY")
news_api_key = os.environ.get("NEWS_API_KEY")


news_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": alpha_vantage_api_key
}
response = requests.get(STOCK_ENDPOINT, params=news_params)
response.raise_for_status()
data = response.json()

# Get Closing Price and Difference Between Price
today_date = dt.datetime.now()
yesterday_date = today_date - dt.timedelta(days=1)
yesterday_closing_price = data["Time Series (Daily)"][yesterday_date.strftime("%Y-%m-%d")]["4. close"]
day_before_yesterday_date = today_date - dt.timedelta(days=2)
day_before_yesterday_closing_price = data["Time Series (Daily)"][day_before_yesterday_date.strftime("%Y-%m-%d")]["4. close"]
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
percentage_difference = (difference / float(day_before_yesterday_closing_price)) * 100
if percentage_difference > 5:
    print("Get News")

news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": news_api_key
    }
news_response = requests.get(NEWS_ENDPOINT, params=news_params)
news_response.raise_for_status()
articles = news_response.json()["articles"]
first_three_articles = articles[:3]

# Send to phone number through Twilio
formatted_articles = [(article["title"], article["description"]) for article in first_three_articles]
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
whatsapp_num = os.environ.get("PHONE_NUMBER")

client = Client(account_sid, auth_token)
for article in formatted_articles:
    message = client.messages \
    .create(
        body=f"Headline: {article[0]}\nBrief: {article[1]}",
        from_="whatsapp:+14155238886",
        to=f"whatsapp:{whatsapp_num}"
    )
    print(message.status)