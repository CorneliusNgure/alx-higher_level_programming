#!/usr/bin/python3
"""Module defines a function that checks if an object"""

def inherits_from(obj, a_class):
    """
    Returns true if object is an instance of a class its inherited from

    Args:
        obj: The object.
        a_class: The class.

    Return:
        True: if obj belongs to inherited class.
        False: otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
