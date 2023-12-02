#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list = my_list
    if idx < 0 or idx >= len(list):
        return my_list
    else:
        list[idx] = element
        return list
