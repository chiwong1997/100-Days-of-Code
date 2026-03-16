import data_manager
from flight_search import FlightSearch

data_manager = data_manager.DataManager()
sheet_data = data_manager.get_destination_data()

print(sheet_data)

# if the IATA code is missing for the first row, we will reupdate the IATA code for all rows
if sheet_data[0]["iataCode"] == "":
    print("The first IATA code is missing, updating IATA codes for the sheet...")
    flight_search = FlightSearch()
    for row in sheet_data:
        city_name = row["city"]
        row["iataCode"] = flight_search.get_destination_code(city_name)
    
    # we update the destination data in the data manager, and then call update_destination_codes to update the Google Sheet
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()