import json


def get_config():

    with open("config/config.json") as file:

        config = json.load(file)

    return config