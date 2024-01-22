#!/usr/bin/python3
"""Module defines a class that checks a function"""


def is_same_class(obj, a_class):
    """
    Checks if an object is an instance of a class

    Args:
        obj: The object to be checked.
        a_class: The class.

    Return:
        True: if the object is instance of class, False otherwise.
    """
    return isinstance(obj, a_class)
