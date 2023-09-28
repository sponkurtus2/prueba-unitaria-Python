# Data input
name = input("What is your name: ")
last_name = input("And your last name: ")

# Map
user = {
    "Name": name,
    "Last_name": last_name
}

file_name = input("File name: ")

with open(f"{file_name}.json", "w+") as file:
    file.write(user)
