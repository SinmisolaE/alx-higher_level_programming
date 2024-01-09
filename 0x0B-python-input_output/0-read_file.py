#!/usr/bin/python3

""" Define mathod read_file"""

def read_file(filename=""):
    """ reads a text file and print to stdout """
    with open(filename, encoding='UTF8') as f:
        print(f.read(), end="")
