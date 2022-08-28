import time

import requests
import datetime as dt
import smtplib

# get the ISS location data
response = requests.get(url="http://api.open-notify.org/iss-now.json")

data = response.json()
longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])

MY_LAT = 12.889994
MY_LONG = 77.648282

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
# Get sunrise and sunset data
sun_data = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
sun_response = sun_data.json()
MY_SUNRISE = int(sun_response["results"]["sunrise"].split("T")[1].split(":")[0])
MY_SUNSET = int(sun_response["results"]["sunset"].split("T")[1].split(":")[0])

time_now = dt.datetime.now()
current_hour = time_now.hour


# send email to me about ISS position
def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="vicknesh@gmail.com", password="asbasjghj@123")
        connection.sendmail(
            from_addr="vicknesh@gmail.com",
            to_addrs="vicknesh@gmail.com",
            msg="Subject: Lookup the sky\n\nThe ISS above you in the sky."
        )


### Check if iss is passing above me
def iss_check():
    if current_hour >= MY_SUNSET or current_hour <= MY_SUNRISE:
        if MY_LAT - latitude >= 0 or MY_LAT - latitude <= 0:
            if MY_LONG - longitude >= 0 or MY_LONG - longitude <= 0:
                print("ISS is above your Head, Look up the sky!!")
                send_email()


### check every 60s about ISS location

while True:
    time.sleep(60)
    iss_check()
    print("Checking ISS position now.")
