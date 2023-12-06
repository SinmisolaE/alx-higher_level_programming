#!/usr/bin/python3
def uniq_add(my_list=[]):
    list = []
    result = 0

    for i in my_list:
        if i in list:
            continue
        else:
            list.append(i)
            result += i
    return result
