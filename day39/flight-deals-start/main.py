# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch

from pprint import pprint
# pretty print --> for nice printing the data
from flight_search import FlightSearch

put_data = DataManager()

sheet_data = put_data.get_data()
if sheet_data[0]['iataCode'] == "":
    put_data.update_iata_codes()

for destination_iata in sheet_data[0]['iataCode']:
    flight_details = FlightSearch()
    result = flight_details.check_flights(origin_city=from_city, destination_city_code=destination_iata,
                                          from_time=date_start, to_time=date_end)

    print(result)
