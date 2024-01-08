#!/usr/bin/python3
"""Defines a class Square """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square inherits from Rectangle """
    def __init__(self, size):
        """ Initializes attribute """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Returns area of square """
        return self.__size ** 2

    def __str__(self):
        """ Printable representation """
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
