import datetime as dt
start = dt.datetime.now()+dt.timedelta(days=1)
start_date = start.strftime("%d/%m/%Y")
end = dt.datetime.now()+dt.timedelta(days=180)
end_date = end.strftime("%d/%m/%Y")
class FlightData:

    def __init__(self):
        self.flight_parameters = {
            "fly_from": "LON",
            "fly_to": "placeholder",
            "date_from": start_date,
            "date_to": end_date,
            "cur": "GBP",
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "max_stopovers": 0,
        }
