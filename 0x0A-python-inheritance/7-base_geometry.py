#!/usr/bin/python3
""" Defines class BaseGeometry """


class BaseGeometry:
    """ The Base class """
    def area(self):
        """ Area method that raises error if no message passes into self """
        if not vars(self):
            raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
