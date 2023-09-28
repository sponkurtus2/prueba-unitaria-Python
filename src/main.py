from utils import file_utils

name = input("What is your name: ")
last_name = input("And your last name: ")

# Map
user = {
    "Name": name,
    "Last_name": last_name
}

file_name = input("File name: ")


file_utils.write_file(file_name, user)

readed_file = file_utils.read_file(file_name)
print(readed_file)
