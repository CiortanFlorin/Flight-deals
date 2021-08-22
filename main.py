from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager


notification_manager = NotificationManager()
flight_data= FlightData()
data_manager = DataManager()
flight_search = FlightSearch(notification_manager)

sheet_data=data_manager.prices

flight_search.location_search(sheet_data)
data_manager.location_update(sheet_data)
flight_search.flight_finder(sheet_data, flight_data.flight_parameters)



