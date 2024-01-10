#!/usr/bin/python3

""" Define function append_write """


def append_write(filename="", text=""):
    """ appends a text to the end of a file """
    with open(filename, 'a', encoding='UTF8') as f:
        return (f.write(text))
