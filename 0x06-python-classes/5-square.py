#!/usr/bin/python3

"""
    Module defines the Square class.


    Classes:
        Square: Represents a square.

    Methods:
        None

    Attributes:
        None
"""


class Square:
    """
    Class represents a square.

    Attributes:
        __size (int): Private instance attribute representing Square's size.

    Methods:
        __init__(self, size=0): Initializes a new instance of the class.
        size(self): Getter method to retrieve the size attribute.
        size(self, value): Setter method to set the size attribute.
        area(self): Computes and returns the area of the square.
        my_print(self): Prints the square with the character #.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        Returns:
            None
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size attribute.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character #.

        Returns:
            None
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
