import datetime
import os
import requests

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("APPKEY")
NUTRITION_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

USER_INPUT = input("Tell me which exercise you did? : ")
GENDER = "male"
WEIGHT = 77
HEIGHT = 173
AGE = 28
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

request_body = {
    "query": USER_INPUT,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}
response = requests.post(url=NUTRITION_ENDPOINT, json=request_body, headers=headers)
exercise_data = response.json()
print(exercise_data)

# collecting required data from the exercise endpoint
exercise_name = exercise_data["exercises"][0]["name"]
exercise_duration = exercise_data["exercises"][0]["duration_min"]
exercise_calories = exercise_data["exercises"][0]["nf_calories"]
workout_name = exercise_name.title()
print(workout_name)
# getting timeframe of the input data

today = datetime.datetime.now()

time = today.now().strftime("%X")
date = today.date().strftime("%d/%m/%Y")

# authenticate to sheety api

SHEETY_ENDPOINT = "https://api.sheety.co/8d7ecb29e352667ea1ea63de4c801700/workoutsTracker/workouts"
SHEETY_TOKEN = "Bearer aGVsbG9fZnJvbV9zaGVldHkK"

headers = {
    "Authorization": "Bearer //masked// {add your key here} //"
}

parameters = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": workout_name,
        "duration": exercise_duration,
        "calories": exercise_calories

    }
}

response = requests.post(url=SHEETY_ENDPOINT, json=parameters, headers=headers)
print(response.json())