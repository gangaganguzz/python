import json
from datetime import datetime
from tripdata import get_trip_details

trips = [
    get_trip_details("Kochi", "15-05-2023", "Enjoyed the beach"),
    get_trip_details("Munnar", "20-06-2023", "Visited tea plantations"),
    get_trip_details("Alappuzha", "10-08-2023", "Enjoyed the houseboat trip")
]

for trip in trips:
    date_object = datetime.strptime(trip["date"], "%d-%m-%Y")
    trip["date"] = date_object.strftime("%B %d, %Y")

json_data = json.dumps(trips, indent=4)
print(json_data)