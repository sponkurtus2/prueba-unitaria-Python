import json


name = input("What is your name: ")
last_name = input("And your last name: ")

# Map
user = {
    "Name": name,
    "Last_name": last_name
}

file_name = input("File name: ")

# Creates a json with the input data

with open(f"{file_name}.json", "w+") as output_file:
    data = json.dumps(user, indent=4)
    output_file.write(data)

# Loads the json file and then print it on the console

with open(f"{file_name}.json", "r") as input_file:
    data = json.load(input_file)
    print(data)
