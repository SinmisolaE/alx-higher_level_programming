#!/usr/bin/python3
"""Define a function add_attribute """


def add_attribute(obj, attribute, value):
    """ adds a new attribute to an object if it’s possible"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
