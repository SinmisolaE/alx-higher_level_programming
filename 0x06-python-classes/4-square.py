#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Representing a Square"""

    def __init__(self, size=0):
        """Initializing the size variable"""
        self.__size = size

    @property
    def size(self):
        """Getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method"""
        self.__size = value
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        return self.__size

    def area(self):
        """Returns the current square area"""
        return (self.__size ** 2)
