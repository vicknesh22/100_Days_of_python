import requests
from flight_data import FlightData

# constants

apikey = "_Yn9lVizvXH23IXkfVnM4jduIDGFXJAV"
kiwi_endpoint = "https://api.tequila.kiwi.com"
meta_apikey = "T_Vu6kEvDP4N9c_OXY5lkOB5lHdbt1Gt"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    # def __init__(self, city_name):
    #     self.city = city_name

    def get_iata_code(self, city_name):
        auth_header = {
            "apikey": apikey
        }
        location_endpoint = f"{kiwi_endpoint}/locations/query"
        json_data = {
            "location_types": "city",
            "Content-Type": "application/json",
            "term": city_name
        }
        response = requests.get(url=location_endpoint, params=json_data,
                                headers=auth_header)
        iata_data_raw = response.json()
        iata_code = iata_data_raw['locations'][0]['code']
        # print(iata_data_raw)
        return iata_code

    def check_flights(self, origin_city, destination_city_code, from_time, to_time):
        headers = {"apikey": meta_apikey}
        query = {
            "fly_from": self.get_iata_code(origin_city),
            "fly_to": destination_city_code,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "INR"
        }

        response = requests.get(
            url=f"{kiwi_endpoint}/v2/search",
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
