#!/usr/bin/python3

"""Defines a function print square """


def print_square(size):

    """ prints square of '#' with size """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print('#' * size)
