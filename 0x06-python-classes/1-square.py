#!/usr/bin/python3

"""
This module defines the Square class.

Attributes:
    size (int): private instance attribute representing the size of the square.

Methods:
    None
"""


class Square:
    """
    This class represents a square.

    Attributes:
        size (int): private instance attribute representing square's size.

    Methods:
        None
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.

        Returns:
            None
        """
        self.__size = size
