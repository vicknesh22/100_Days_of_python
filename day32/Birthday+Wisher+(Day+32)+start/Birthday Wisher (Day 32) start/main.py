# import smtplib
#
# my_email = "vicknesh22@gmail.com"
# my_password = "abcdef123%"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="vicknesh/r@example.in",
#         msg="Subject:Hello\n\nThis is the body of the email."
#     )
#
#
# import datetime as dt
#
# now = dt.datetime.now()
# print(now)
# year = now.year
# print(year)
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1994, month=3, day=22)
# print(date_of_birth)

# step one : getting the current date and time

import datetime as dt
import random
import smtplib

current_date = dt.datetime.now()
day_of_week = current_date.weekday()

with open("quotes.txt", "r") as quotes_data:
    quotes = quotes_data.read().splitlines()
    random_quote = random.choice(quotes)

print(random_quote)
if day_of_week == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="vicknesh@gmail.com", password="ABCDDEF4@")
        connection.sendmail(
            from_addr="vicknesh@gmail.com",
            to_addrs="test@example.com",
            msg=f"Subject:Motivation-Quotes\n\n{random_quote}"
        )
