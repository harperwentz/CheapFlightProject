import requests
from pprint import pprint

GOOGLESHEET_ENDPOINT = "https://api.sheety.co/35fadeb69b4aa9fdb979f5d4a6dc4a48/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.get_sheet_data()




    def get_sheet_data(self):
        r = requests.get(f"{GOOGLESHEET_ENDPOINT}")
        r.raise_for_status()
        google_sheet_data = r.json()
        google_sheet_data = google_sheet_data["prices"]
        return google_sheet_data

    def update_IATA_code(self, row_id, IATA_code):
        self.update_code_endpoint = f"{GOOGLESHEET_ENDPOINT}/{row_id}"
        update_iata = {
            "price": {
                "iataCode": IATA_code
            }
        }
        response = requests.put(url=self.update_code_endpoint, json=update_iata)
        return response

