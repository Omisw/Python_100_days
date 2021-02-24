import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

api_key = "API_KEY"
MY_LAT = 20.659698
MY_LONG = -103.349609

account_sid = "SID_ACOUNT_KEY"
auth_token = "AUTH_TOKEN_KEY"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False

for hour_weather in data["hourly"][:12]:
    id_weather = hour_weather["weather"][0]["id"]
    if id_weather < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body = "It's going to rain today. Remember to bring an umbrella ☂️",
        from_= "+FROM_WICH_NUMBER",
        to = "+PHONE_NUMBER_TO_SEND"
    )
    print(message.status)