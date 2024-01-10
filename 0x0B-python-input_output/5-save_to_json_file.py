#!/usr/bin/python3
import json
""" Define function save_to_json_file"""


def save_to_json_file(my_obj, filename=""):
    """writes object to file """
    with open(filename, 'w', encoding="UTF8") as f:
        json.dump(my_obj, f)
