import requests


def check_flights():
    headers = {"apikey": "T_Vu6kEvDP4N9c_OXY5lkOB5lHdbt1Gt"}
    query = {
        "fly_from": "LON",
        "fly_to": "JFK",
        "date_from": "28/09/2022",
        "date_to": "28/03/2023",
        "nights_in_dst_from": 7,
        "nights_in_dst_to": 28,
        "flight_type": "round",
        "one_for_city": 1,
        "max_stopovers": 0,
        "curr": "INR"
    }

    response = requests.get(
        url=f"https://api.tequila.kiwi.com/v2/search",
        headers=headers,
        params=query,
    )
    return response.json()


print(check_flights())
