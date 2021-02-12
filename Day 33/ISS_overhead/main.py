import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 20.659698  # Your latitude
MY_LONG = -103.349609  # Your longitude

EMAIL = "pruebasomis@gmail.com"
PASSWORD = "themoonblue"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour_now = time_now.hour
print(f"Hour in my country: {hour_now}, sunrise: {sunrise}, sunset: {sunset}")

while True:
    time.sleep(60)
    print(iss_latitude, iss_longitude)
    if (iss_latitude <= MY_LAT + 5 and iss_latitude >= MY_LAT -5) and (iss_longitude <= MY_LONG + 5 and iss_longitude >= MY_LONG - 5):
        print("ISS is close")
        if hour_now < sunrise and hour_now > sunset:
            print("ISS is close")
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(EMAIL, PASSWORD)
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs="webomis@yahoo.com",
                    msg="Subject: International Space Station is close to your location\n\nThe International Space Station is close to your location, go outside and look to the sky."
                )

