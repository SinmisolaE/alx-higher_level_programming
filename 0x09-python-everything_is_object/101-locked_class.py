#!/usr/bin/python3

""" Defines a class LockedClass """

class LockedClass:
    """ No other instance should be created apart from firstname """
    __slots__ = ('first_name')
