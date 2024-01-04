#!/usr/bin/python3

""" Defines a class Rectangle """


class Rectangle:
    """ Representing a rectangle """

    def __init__(self, width=0, height=0):
        """ Initializing attributes """

        self.__height = height
        self.__width = width

    @property
    def height(self):
        """ Getter method fir height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Setter that assigns value to height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ Getter for width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Assigns value to width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
