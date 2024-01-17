#!/usr/bin/python3

"""This module defines the function, print_square(size):"""


def print_square(size):
    """
    Prints the square with the character, #
    Args:
        size (int): size length of the square
    Raises:
        TypeError: specified TypeError if size isn't an int.
                 : specified TypeError if size is float and < 0
        ValueError: specified ValueError if size < 0
    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
