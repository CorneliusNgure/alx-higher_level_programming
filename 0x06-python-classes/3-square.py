#!/usr/bin/python3

"""
    This module defines the Square class.

    Functionality for handling square-related operations.

    Classes:
        Square: Represents a square.

    Attributes:
        None

    Methods:
        Square.__init__(self, size=0): Initializes a new instance of the class.
        Square.area(self): Computes and returns the square area.

    Exceptions:
        TypeError: Raised if size is not an integer during initialization.
        ValueError: Raised if size is less than 0 during initialization.
    """

class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): private instance attribute representing square's size.

    Methods:
        __init__(self, size=0): initializes a new instance of class.
        area(self): computes and returns the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): the size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        Returns:
            None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        computes and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
