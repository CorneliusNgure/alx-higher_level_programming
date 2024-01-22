#!/usr/bin/python3
"""Defines a class that checks a function"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a class or inherited class

    Args:
        obj: The object.
        a_class: The class.

    Return:
        True: if object is an instance of a class or inherited class
        False: otherwise.
    """

    return isinstance(obj, a_class)
