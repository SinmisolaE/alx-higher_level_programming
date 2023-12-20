#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Representing a Square"""

    def __init__(self, size=0):
        """Initializing size considering exception"""
        if not isinstance(size, int):
            print("size must be an integer")
        elif size < 0:
            print("size must be >= 0")
        self.__size = size

    def area(self):
        """Return square area"""
        return (self.__size ** 2)
