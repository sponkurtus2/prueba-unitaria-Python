import json


def write_file(file_name, input_data):
    with open(f"{file_name}.json", "w+") as output_file:
        data = json.dumps(input_data, indent=4)
        output_file.write(data)


def read_file(file_name):
    with open(f"{file_name}.json", "r") as input_file:
        return json.load(input_file)
