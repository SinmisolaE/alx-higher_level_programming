#!/usr/bin/python3

""" Define method write_file """


def write_file(filename="", text=""):
    with open(filename, 'w', encoding='UTF8') as f:
        return(f.write(text))
