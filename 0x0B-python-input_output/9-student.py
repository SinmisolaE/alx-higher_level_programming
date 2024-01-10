#!/usr/bin/python3
""" Define a class Student """


class Student:
    """ Defines a student """
    def __init__(self, first_name, last_name, age):
        """ Initializes attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Returns dictionary representation
        of Student instance"""
        return self.__dict__
