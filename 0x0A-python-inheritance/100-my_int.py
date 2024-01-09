#!/usr/bin/python3
""" Define class MyInt """


class MyInt(int):
    """ MyInt is a rebel. MyInt has == and != operators inverted """
    def __new__(cls, *args, **kwargs):
        """ create new instance of the class """
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """ Checks if objects are equal """
        return int(self) != other

    def __ne__(self, other):
        """ method for non equal """
        return int(self) == other
