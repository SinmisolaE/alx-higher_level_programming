#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    if a_dictionary is None:
        return None
    else:
        for i in a_dictionary:
            if a_dictionary[i] > max:
                max_list = i
                max = a_dictionary[i]
        return max_list
