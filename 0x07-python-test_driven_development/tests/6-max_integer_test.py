#!/usr/bin/python3
""" Unit test for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TextMaxInteger(unittest.TestCase):
    """ tester class forcases passed to the function """

    def test_unsort_list(self):
        """ Test a list with values unordered """
        list = [6, 12, 9, 3]
        self.assertEqual(max_integer(list), 12)

    def test_sort_list(self):
        """ Test a list with values ordered """
        list = [3, 7, 56, 66]
        self.assertEqual(max_integer(list), 66)

    def test_max_first(self):
        """ Test list with max at the beginning """
        list = [9, 5, 6, 1]
        self.assertEqual(max_integer(list), 9)

    def test_empty_list(self):
        """ Test an empty list """
        list = []
        self.assertEqual(max_integer(list), None)

    def test_single_elem(self):
        """ Test on a list of one ekem """
        list = [5]
        self.assertEqual(max_integer(list), 5)

    def test_flooats(self):
        """ Tests on list of floats """
        list = [3.6, 7.3, 9.9]
        self.assertEqual(max_integer(list), 9.9)

    def test_int_and_float(self):
        """ Tests on list of both lists and floats """
        list = [9.7, -5, 10, 5.5]
        self.assertEqual(max_integer(list), 10)

    def test_string(self):
        """ Tests  on string """
        string = "Free"
        self.assertEqual(max_integer(string), 'r')

    def test_list_string(self):
        """ Tests on a list of string """
        list = ["name", "age", "height"]
        self.assertEqual(max_integer(list), "name")

    def test_empty_string(self):
        """ Tests on an empty string """
        string = ""
        self.assertEqual(max_integer(string), None)

if __name__ == '__main__':
    unittest.main()
