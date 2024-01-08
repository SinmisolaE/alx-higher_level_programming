#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Representing a Square"""
    def __init__(self, size=0):
        """Initializes size"""
        self.__size = size

    @property
    def size(self):
        """Getter method of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method of size"""
        self.__size = value
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        return self.__size

    def area(self):
        """Return current square area"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints a square of '#' size by size"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)
