#!/usr/bin/python3
def max_integer(my_list=[]):
    x = 0
    if my_list is None:
        return
    for i in my_list:
        if i > x:
            x = i
    return x
