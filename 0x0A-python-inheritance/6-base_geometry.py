#!/usr/bin/python3
""" Defines class BaseGeometry """


class BaseGeometry:
    """ The Base class """
    def area(self):
        """ Area method that raises error if no message passes into self """
        raise Exception("area() is not implemented")
