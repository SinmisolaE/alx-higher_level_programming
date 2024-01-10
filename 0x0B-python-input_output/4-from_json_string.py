#!/usr/bin/python3
import json

""" Define function from_json_string """


def from_json_string(my_str):
    """ returns object from conversion of json string """
    return (json.loads(my_str))
