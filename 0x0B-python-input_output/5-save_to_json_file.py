#!/usr/bin/python3
""" Define function save_to_json_file"""
import json


def save_to_json_file(my_obj, filename=""):
    """writes object to file """
    with open(filename, 'w', encoding="UTF8") as f:
        json.dump(my_obj, f)
