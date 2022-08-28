import csv
import requests
import pandas
from pprint import pprint
from flight_data import FlightData
from data_manager import DataManager
API_KEY = "denNp7WXfvME2YqxPBvCvLoTOSiZ6Q_J"
CODE_ENDPOINT = f"https://tequila-api.kiwi.com"



class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def get_IATA_codes(self, city_name):
        location_endpoint = f"{CODE_ENDPOINT}/locations/query"
        headers = {"apikey": API_KEY}
        query = {"term": city_name, "location_types": "city"}
        iata_request = requests.get(url=location_endpoint, headers=headers, params=query)
        iata_request.raise_for_status()
        city_data = iata_request.json()["locations"]
        iata_code = city_data[0]["code"]
        return iata_code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            url=f"{CODE_ENDPOINT}/v2/search",
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





