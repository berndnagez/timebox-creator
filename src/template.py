import json


def read_template(file_path):
    with open(file_path, 'r') as file:
        template = json.load(file)
    return template
