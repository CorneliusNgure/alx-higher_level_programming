#!/usr/bin/python3

"""
Defines a square class

Classes:
        Square: Represents a square.

    Attributes:
        None

    Methods:
        Square.__init__(self, size=0): initializes a new instance of class.

    Exceptions:
        TypeError: Raised if size is not an integer.
        ValueError: Raised if size is less than 0.
    """


class Square:
    """
    This class represents a square.

    Basic structure for handling square-related operations.

    Attributes:
        __size (int): private instance attribute representing square's size.

    Methods:
        __init__(self, size=0): Initializes a new instance of the Square class.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square. Defaults to 0.

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
