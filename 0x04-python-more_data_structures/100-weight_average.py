#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum = 0
    div = 0
    for i in my_list:
        mul = i[0] * i[1]
        sum += mul
        div += i[1]
    result = sum / div
    return result
