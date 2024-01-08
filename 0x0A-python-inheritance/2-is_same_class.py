#!/usr/bin/python3
""" Defines a function is_same_class """


def is_same_class(obj, a_class):
    """ Returns True if obj is instance of a_class"""
    if type(obj) is a_class:
        return True
    return False
