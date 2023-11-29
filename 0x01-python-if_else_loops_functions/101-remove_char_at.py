#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    i = 0
    for x in str:
        if i != n:
            new += x
        i += 1
    return new
