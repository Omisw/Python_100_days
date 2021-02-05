import smtplib
import datetime
import random

my_email = "pruebasomis@gmail.com"
password = "themoonblue"
# password = "ajcaixymfwsnqihk"

now = datetime.datetime.now()
day_of_week = now.weekday()

if day_of_week == 1:
    with open("quotes.txt") as data_file:
        motivational_quotes = data_file.readlines()
        random_quote = random.choice(motivational_quotes)
        print(random_quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="webomis@yahoo.com",
            msg=f"Subject:Motivational day.\n\n{random_quote}"
        )
