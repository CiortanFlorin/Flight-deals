import requests
from notification_manager import NotificationManager
url = "https://tequila-api.kiwi.com/locations/query"
flights_url = "https://tequila-api.kiwi.com/v2/search"
apikey = "YOUR FLIGHT NEWS API KEY"

header = {
    "apikey": apikey,
}
parameters = {
    "term": "place_holder",
    "location_types": "city",
    "locale": "en-US",
}

class FlightSearch:
    def __init__(self, notification_manager: NotificationManager):
        self.client = notification_manager
        self.parameters = {
    "term": "place_holder",
    "location_types": "city",
    "locale": "en-US",
}


    def location_search(self, updated_list):
        for x in updated_list:
            self.parameters["term"]=x["city"]
            r=requests.get(url=url, params=self.parameters, headers=header)
            data=r.json()
            x["iataCode"] = data["locations"][0]["code"]

    def flight_finder(self, update_list, flight_details):
        for x in update_list:
            flight_details["fly_to"] = x["iataCode"]
            q = requests.get(url=flights_url, params=flight_details, headers=header)
            data = q.json()
            try:
                flights = data['data'][0]
            except IndexError:
                flights = {}
            else:
                price = flights['price']
                arrival_city = flights['cityTo']
                departure_city = flights["cityFrom"]
                arrival_airport_code = flights["cityCodeTo"]
                departure_city_code = flights["cityCodeFrom"]
                inbound_date = (flights["local_departure"].split("T"))[0]
                outbound_date = (flights['route'][1]["local_departure"].split("T"))[0]
                text = f"Low price alert! Only £{price} to fly from {departure_city}-{departure_city_code} to {arrival_city}-{arrival_airport_code} from {inbound_date} to {outbound_date}"
                print(text)
            if x["lowestPrice"] > price:
                self.client.send_msg(text)