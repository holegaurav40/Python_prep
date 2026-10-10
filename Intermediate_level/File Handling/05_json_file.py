#json file handling

import json #impoert json module

student = {         #store data in dictionary format
    "name": "Rahul",
    "age": 20
}

# Write data to JSON file
with open("student.json", "w") as file:
    json.dump(student, file)

# Read data from JSON file
with open("student.json", "r") as file:
    data = json.load(file)

print(data)
print(data["name"])