#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for i in matrix:
        print(' '.join("{:d}".format(x)for x in i))
