#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict = list(a_dictionary.keys())
    dict.sort()
    for i in dict:
        print("{}: {}".format(i, a_dictionary.get(i)))
