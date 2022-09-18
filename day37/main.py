# pixela project
import requests
import datetime as dt

# constants
USERNAME = "vicknesh"
TOKEN = "aGVsbG9waXhlbGEK"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
    "thanksCode": "hello"
}

# one time code to create new user

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# {"message":"Success. Let's visit https://pixe.la/@vicknesh , it is your profile page!","isSuccess":true}

# Graph api

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": "graph1",
#     "name": "running",
#     "unit": "Km",
#     "type": "float",
#     "color": "ichou"
# }
#
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# add new pixel to graph

GRAPH_ID = "graph1"

ADD_PIXEL_ENDPOINT = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
RUN_KMS = "14"

# Method 1

# now = dt.datetime.now()
# date_sign = str(now.date())
# today_date = date_sign.replace("-", "")

# Method 2

today = dt.datetime.now()
today_date = today.strftime("%Y%m%d")


headers = {
    "X-USER-TOKEN": TOKEN
}

add_pixel_config = {
    "date": today_date,
    "quantity": RUN_KMS
}
# to create a new pixel
# response = requests.post(url=ADD_PIXEL_ENDPOINT, json=add_pixel_config, headers=headers)
# print(response.text)

# to delete or update the existing date point
DATE = "20220917"
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"
update_pixel_config = {
    "date": "20220917",
    "quantity": "4.39"
}
response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
print(response.text)