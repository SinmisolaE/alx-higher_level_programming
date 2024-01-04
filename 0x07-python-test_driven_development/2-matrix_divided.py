#!/usr/bin/python3

""" Defines a method matrix_divided """


def matrix_divided(matrix, div):

    """ Returns a list of result of dividing maxtrix by div """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(x, list) for x in matrix) or
            not all(isinstance(i, int) or isinstance(i, float)
                    for x in matrix for i in x)):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if not all(len(matrix[0]) == len(i) for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if (not isinstance(div, int) and not isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
