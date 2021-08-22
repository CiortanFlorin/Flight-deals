import requests

url = 'https://api.sheety.co/ff0013d9959b39c8e0833686ad544b78/cheapFlights/prices'
update_url = "https://api.sheety.co/ff0013d9959b39c8e0833686ad544b78/cheapFlights/prices/"

class DataManager:
    def __init__(self):
        self.r = requests.get(url)
        self.data = self.r.json()
        self.prices = self.data["prices"]
        self.parameters = {}

    def location_update(self, fligts_list):
        for x in fligts_list:
            self.parameters = {
                "price": {
                    "iataCode": x["iataCode"]

                }
            }
            id = x["id"]
            export=requests.put(url=f"{update_url}{id}", json=self.parameters)
            print(export.text)
