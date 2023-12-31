#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Representing a Square"""

    def __init__(self, size=0):
        """Initializing variable size but considering errors"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
