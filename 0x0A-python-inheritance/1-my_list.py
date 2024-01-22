#!/usr/bin/python3

"""Module of MyList class that inherits from the builtin, list"""


class MyList(list):
    """Implements inheritance and prints in sorted order"""

    def print_sorted(self):
        """Prints list in sorted(ascending) order"""
        sorted_list = sorted(self)
        print(sorted_list)
