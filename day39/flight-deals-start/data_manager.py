import requests
from flight_search import FlightSearch

# constants
SHEETY_ENDPOINT = "https://api.sheety.co/8d7ecb29e352667ea1ea63de4c801700/flightDeals/prices"
AUTH_TOKEN = "Bearer aGVsbG9ndXlzCg=="

auth_header = {
    "Authorization": AUTH_TOKEN
}


class DataManager:
    def __init__(self):
        self.row_number = ""
        self.payload = ""
        self.endpoint = SHEETY_ENDPOINT
        self.auth = auth_header

    # for getting data from the sheet
    def get_data(self):
        get_response = requests.get(url=self.endpoint, headers=self.auth)
        data = get_response.json()
        data = data["prices"]
        return data

    # This class is responsible for talking to the Google Sheet.

    def update_iata_codes(self):
        sheet_data = self.get_data()
        # get data
        for entry in sheet_data:
            city_name = entry["city"]
            iata_codes = FlightSearch()
            entry['iataCode'] = iata_codes.get_iata_code(city_name)
            self.row_number = entry['id']
            iata_code_value = entry['iataCode']

            self.payload = {
                "price": {
                    "iataCode": iata_code_value
                }
            }
            response = requests.put(url=f"{self.endpoint}/{self.row_number}", json=self.payload, headers=self.auth)

            #print(response.text)


