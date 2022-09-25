# import requests
# from data_manager import DataManager
# from flight_search import FlightSearch
#
# # constants
#
# apikey = "_Yn9lVizvXH23IXkfVnM4jduIDGFXJAV"
# kiwi_endpoint = "https://api.tequila.kiwi.com"
#
#
# class FlightData:
#     # This class is responsible for structuring the flight data.
#     def __init__(self, current_city, from_date, to_date):
#         self.current_city = current_city
#         self.date_from = from_date
#         self.date_to = to_date
#
#     def get_flight_prices(self):
#         flight_price_endpoint = f"{kiwi_endpoint}/v2/search"
#
#         auth_header = {
#             "apikey": apikey
#         }
#         parameters = {
#             "fly_from": self.current_city,
#             "date_from": self.date_from,
#             "date_to": self.date_to
#
#         }
#
#         response = requests.get(url=flight_price_endpoint, params=parameters, headers=auth_header)
#         return response.json()

class FlightData:

    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date,
                 return_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
