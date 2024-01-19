#!/usr/bin/python3
"""Unittests for the max_integer(list=[]) function"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines unittests for the max_integer(list=[]) function"""

    def test_ordered_list(self):
        """Test an ordered list of ints"""
        ordered = [45, 46, 47, 48]
        self.assertEqual(max_integer(ordered), 48)

    def test_unordered_list(self):
        """Test an unordered list of ints"""
        unordered = [173, 98, 4897, 3]
        self.assertEqual(max_integer(unordered), 4897)

    def test_max_at_first_index(self):
        """Test a list with a max value at index[0]"""
        max_at_first_index = [56, 3, 23, 1]
        self.assertEqual(max_integer(max_at_first_index), 56)

    def test_empty_list(self):
        """Test an empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element"""
        element = [98]
        self.assertEqual(max_integer(element), 98)

    def test_floats(self):
        """Test a list of floats"""
        floats = [41.93, 8.983, -10.3, 7.543]
        self.assertEqual(max_integer(floats), 41.93)

    def test_ints_and_floats(self):
        """Test a list of ints and floats"""
        ints_and_floats = [1, 85.8, -87, 55, 4]
        self.assertEqual(max_integer(ints_and_floats), 85.8)

    def test_string(self):
        """Test strings"""
        string = "Cornelius"
        self.assertEqual(max_integer(string), 'u')

    def test_list_of_strings(self):
        """Test a list of strings"""
        strings = ["Cornelius", "Ngure", "Muthoni", "Mike"]
        self.assertEqual(max_integer(strings), "Ngure")

    def test_empty_string(self):
        """Test an empty string"""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
