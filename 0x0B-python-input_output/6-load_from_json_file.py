#!/usr/bin/python3
""" Define load_from_json_file """
import json


def load_from_json_file(filename):
    """ creates an object from a json file """
    with open(filename, encoding='UTF8') as f:
        return (json.loads(f.read()))
