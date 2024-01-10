#!/usr/bin/python3
""" Define function to_json_string """


import json


def to_json_string(obj):
    """ returns JSON representation of object which is string """

    return (json.dumps(obj))
