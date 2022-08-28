from time import strftime

import requests
from datetime import datetime, timedelta

API_KEY = "denNp7WXfvME2YqxPBvCvLoTOSiZ6Q_J"
CODE_ENDPOINT = f"https://tequila-api.kiwi.com"

DATE_FROM = datetime.today() + timedelta(days=1)
DATE_TO = DATE_FROM + timedelta(days=180)
#DATE_FROM = str(DATE_FROM)
#DATE_TO = str(DATE_TO)
DATE_FROM = DATE_FROM.strftime("%d/%m/%Y")
DATE_TO = DATE_TO.strftime("%d/%m/%Y")


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

    def get_prices(self, iata_code):
        search_endpoint = f"{CODE_ENDPOINT}/search"
        headers = {"apikey": API_KEY}
        query = {"fly_from": "CPH",
                 "fly_to": iata_code,
                 "date_from": DATE_FROM,
                 "date_to": DATE_TO,
                 "nights_in_dst_to": 27,
                 "flight_type": "round"
                 }
        flight_request = requests.get(url=search_endpoint, headers=headers, params=query)
        flight_request.raise_for_status()
        flight_data = flight_request.json()["data"]
        price = flight_data[4]["price"]
        return price