##################### Extra Hard Starting Project ######################
import random
import smtplib

import pandas
import datetime as dt

# 1. Update the birthdays.csv
birthdays_csv = pandas.read_csv("birthdays.csv")
print(birthdays_csv)
birthdays_date = birthdays_csv["day"].to_dict()
birthdays_month = birthdays_csv["month"].to_dict()
birthdays_date_list = []
birthdays_month_list = []
for day in birthdays_date.items():
    birthdays_date_list.append(day[1])

print(birthdays_date_list)

for month in birthdays_month.items():
    birthdays_month_list.append(month[1])

print(birthdays_month_list)

# 2. Check if today matches a birthday in the birthdays.csv

now = dt.datetime.now()
this_month = now.month
today = now.day


def send_wishes():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="vicknesh@gmail.com", password="ABCDDEF4@")
        connection.sendmail(
            from_addr="vicknesh@gmail.com",
            to_addrs="test@example.com",
            msg=f"Subject:Happy-Birthday\n\n{final_template}"
        )


if this_month in birthdays_month_list:
    if today in birthdays_date_list:
        # send_wishes()
        recipient = birthdays_csv[f"day={today}"]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

template = []
with open("./letter_templates/letter_1.txt", "r") as template_data1:
    template1 = template_data1.read()
    template.append(template1)
with open("./letter_templates/letter_2.txt", "r") as template_data2:
    template2 = template_data2.read()
    template.append(template2)
with open("./letter_templates/letter_3.txt", "r") as template_data3:
    template3 = template_data3.read()
    template.append(template3)

final_template = random.choice(template)

# 4. Send the letter generated in step 3 to that person's email address.
print(final_template)
