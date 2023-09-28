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
