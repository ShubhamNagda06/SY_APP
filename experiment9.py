import csv
import json

records = []

with open('students.csv', 'r') as f:
    reader = csv.DictReader(f)

    for row in reader:
        records.append(row)

with open('students.json', 'w') as out:
    json.dump(records, out, indent=4)

print("CSV data converted to JSON successfully")