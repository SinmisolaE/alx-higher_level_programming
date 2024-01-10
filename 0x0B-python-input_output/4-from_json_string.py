#!/usr/bin/python3
""" Define function from_json_string """


import json


def from_json_string(my_str):
    """ returns object from conversion of json string """
    return (json.loads(my_str))
