import requests
from datetime import date, timedelta
import os
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT_API = "https://www.alphavantage.co/support/#api-key"
NEWS_ENDPOINT_API = "https://newsapi.org/"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_ENDPOINT_API
}

response_stock = requests.get("https://www.alphavantage.co/query", parameters)
stock_data = response_stock.json()

# Dates
now = date.today()
yesterday = str(now - timedelta(days=1))
before_yesterday = str(now - timedelta(days=2))

yesterday_closes = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
print(yesterday_closes)
before_yesterday_closes = float(stock_data["Time Series (Daily)"][before_yesterday]["4. close"])
print(before_yesterday_closes)

difference_closing = abs(yesterday_closes - before_yesterday_closes)
percentage_stock = float(before_yesterday_closes * .015)


url = ('http://newsapi.org/v2/everything?'
       f'q={COMPANY_NAME}&'
       f'from={now}&'
       'sortBy=popularity&'
       f'apiKey={NEWS_ENDPOINT_API}'
       )

response = requests.get(url)
news_data = response.json()
news_list = news_data["articles"][:3]

account_sid = 'https://www.twilio.com/'
auth_token = 'https://www.twilio.com/'
client = Client(account_sid, auth_token)
print(f"{news_list[1]['title']}\n{news_list[1]['description']}")

if percentage_stock < difference_closing:
    message = client.messages \
        .create(
            body=f"{news_list[1]['title']}\n{news_list[1]['description']}",
            from_='Your Twilio number',
            to='Number to send'
            )
    print(message.sid)


