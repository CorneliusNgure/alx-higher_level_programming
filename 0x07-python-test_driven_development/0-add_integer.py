#!/usr/bin/python3
"""
Function that returns addition of 2 ints
"""


def add_integer(a, b=98):
    """
    Returns:
        int: Addition of two ints

    Args:
        a (int or float): First argument.
        b (int or float): Second argument.

    Raises:
        TypeError: If the args are not ints or floats.
    """

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
