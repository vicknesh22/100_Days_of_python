import requests
import os
from twilio.rest import Client
import datetime as dt

# open weather keys
api_key = os.environ.get("API_KEY")
api_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

# twilio keys
account_sid = os.environ.get("TW_ACC")
auth_token = os.environ.get("AUTH_TOKEN")
# failsafe twillio - 8aT27yZRgmsaFftJ9_k9dKMdebtVhB4M6Y4W6eIK

# https://api.openweathermap.org/data/2.5/weather?lat=12.87&lon=77.64&appid=f21717f59b3b451efdfe9d808a49d706
# https://api.openweathermap.org/data/3.0/onecall?lat=12.87&lon=77.64&appid=a4ed7f5b3a194f20f9190a3947efddd2
# https://api.openweathermap.org/data/2.5/onecall?lat=12.87&lon=77.64&appid=a4ed7f5b3a194f20f9190a3947efddd2

parameters = {
    "lat": 12.87,
    "lon": 77.64,
    "appid": api_key,
    "units": "metric"
}

response = requests.get(api_endpoint, params=parameters)
response.raise_for_status()
response_json = response.json()
weather_data_rain = response_json["hourly"]

# # using enumerate to get the index number of the list as we're looping through it
# for index, hours in enumerate(weather_data_rain):
#     if index < 12:
#         for hour in hours['weather']:
#             weather_code = int(hour['id'])
#
#             if weather_code >= 500 and weather_code < 600:
#                 print(f"{weather_code} - Bring an Umberlla today! It may rain ")

# method 2 - using the slice operator to slice the list
weather_slice = weather_data_rain[0:12]

for hour_data in weather_slice:
    weather_code = hour_data["weather"][0]["id"]
    if int(weather_code) < 700:
        will_it_rain = True
will_it_rain = False

if will_it_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella ☂️.",
        from_='+17075173593',
        to='+918012895962'
    )

    print(message.status)


