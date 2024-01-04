#!/usr/bin/python3

""" Defines a class Rectangle """


class Rectangle:
    """ Representing a Rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Initializing attributes """
        type(self).number_of_instances += 1
        self.height = height
        self.width = width

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
        return (self.__height)

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
        return (self.__width)

    def area(self):
        """ Returns area of the rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Returns perimeter of rectangle
        but if any side is 0, perimeter is 0"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Finds the rectangle with larger area error if not object"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """ Returns the printable representation of class Rectangle """
        if self.__width == 0 or self.__height == 0:
            return ""
        hash = []
        for i in range(self.__height):
            [hash.append(str(self.print_symbol)) for x in range(self.__width)]
            if i != self.__height - 1:
                hash.append("\n")
        return ("".join(hash))

    def __repr__(self):
        """ Return the string representation of Rectangle """
        rep = "Rectangle(" + str(self.__width)
        rep += ", " + str(self.__height) + ")"
        return rep

    def __del__(self):
        """ Fuction called when an instance is deleted """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
