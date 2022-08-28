#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from datetime import datetime, timedelta
import csv
import pandas
from pprint import pprint
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_sheet_data()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "CPH"

if sheet_data[0]["iataCode"] == "":
    for row in range(len(sheet_data)):
        city_name = sheet_data[row]["city"]
        row_id = sheet_data[row]["id"]
        iata_code = flight_search.get_IATA_codes(city_name)
        data_manager.update_IATA_code(row_id, iata_code)
    data_manager.destination_data = sheet_data
    data_manager.update_IATA_code()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )


# for city in range(len(sheet_data)):
#     city_name = sheet_data[city]["city"]
#     row_id = sheet_data[city]["id"]
#     iata_code = flight_search.get_IATA_codes(city_name)
#     price = flight_data.get_prices(iata_code)
#     print(f"{iata_code}: {price}")





