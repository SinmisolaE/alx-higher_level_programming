#!/usr/bin/python3

""" Defines class MyList """


class MyList(list):
    """ Inherits list and it's sorted content """

    def print_sorted(self):
        """ Print sorted """
        new = sorted(self)
        print(new)
