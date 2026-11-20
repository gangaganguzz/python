import json
from datetime import datetime
from tracker import get_travel_record

records = [
    get_travel_record("Kochi", "Enjoyed the beach", "05-06-2022"),
    get_travel_record("Munnar", "Visited tea plantations", "15-07-2022"),
    get_travel_record("Alappuzha", "Enjoyed houseboat trip", "20-08-2022")
]

for record in records:
    date_object = datetime.strptime(record["date"], "%d-%m-%Y")
    record["date"] = date_object.strftime("%B %d, %Y")

json_data = json.dumps(records, indent=4)
print(json_data)

parsed_data = json.loads(json_data)

for record in parsed_data:
    print(record)