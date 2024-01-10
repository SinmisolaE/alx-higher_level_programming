#!/usr/bin/python3
import json


""" Define load_from_json_file """


def load_from_json_file(filename):
    """ creates an object from a json file """
    with open(filename, encoding='UTF8') as f:
        return (json.loads(f.read()))
