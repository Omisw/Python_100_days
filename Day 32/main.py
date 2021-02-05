import datetime as dt
import pandas
import random
import smtplib

email = "correo@gmail.com"
password = "password_email"

now = dt.datetime.now()
today = (now.month, now.day)

birthdays_data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): [data_row["name"], data_row["email"]] for (index, data_row) in birthdays_data.iterrows()}

r_num = random.randint(1, 3)
if today in birthdays_dict:
    with open(f"letter_templates/letter_{r_num}.txt") as birthday_file:
        birthday_letter = birthday_file.read()
        birthday_name = birthdays_dict[today][0]
        new_letter = birthday_letter.replace("[NAME]", birthday_name)
        # with open(f"letter_templates/letter_{birthday_name}.txt", mode="w") as letter_file:
        #     letter_file.write(new_letter)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(
            from_addr=email,
            to_addrs=birthdays_dict[today][1],
            msg=f"Subject: Happy birthday!\n\n{new_letter}"
        )
