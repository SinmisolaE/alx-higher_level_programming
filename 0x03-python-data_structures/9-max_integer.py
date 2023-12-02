#!/usr/bin/python3
def max_integer(my_list=[]):
    x = 0
    if my_list == None:
        return None
    for i in range(len(my_list)):
        if my_list[i] > x:
            x = my_list[i]
    return x
