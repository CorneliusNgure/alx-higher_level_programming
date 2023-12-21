#!/usr/bin/python3

"""
This module defines the Square class.

A square is a geometric shape with four equal sides and four equal angles.

Classes:
    Square: Represents a square.

Methods:
    None

Attributes:
    None
"""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (float/int): Private instance attribute of Square's size.

    Methods:
        __init__(self, size=0): Initializes a new instance of class.
        size(self): Getter method to retrieve the size attribute.
        size(self, value): Setter method to set the size attribute.
        area(self): Computes and returns the area of the square.
        __eq__(self, other): Checks if two squares are equal in area.
        __ne__(self, other): Checks if two squares are not equal in area.
        __gt__(self, other): Checks if area of the current square is > another.
        __ge__(self, other): Checks if area the square is >= equal to another.
        __lt__(self, other): Checks if area of square is < than to another.
        __le__(self, other): Checks if area of square is <= to the of another.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (float or int, optional):the size of square. Defaults to 0.

        Raises:
            TypeError: If size is not a number.
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
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size attribute.

        Args:
            value (float or int): The new size value.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.

        Returns:
            None
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks if two squares are equal in area.

        Args:
            other (Square): Another square.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return (
                self.area() == other.area()
                ) if isinstance(other, Square) else False

    def __ne__(self, other):
        """
        Checks if two squares are not equal in area.

        Args:
            other (Square): Another square.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """
        Checks if area of the current square is > area of another square.

        Args:
            other (Square): Another square.

        Returns:
            bool: True if the area is greater, False otherwise.
        """
        return (
                self.area() > other.area()
                ) if isinstance(other, Square) else False

    def __ge__(self, other):
        """
        Checks if area of current square >= the area of another square.

        Args:
            other (Square): Another square.

        Returns:
            bool: True if the area is greater than or equal, False otherwise.
        """
        return (
                self.area() >= other.area()
                ) if isinstance(other, Square) else False

    def __lt__(self, other):
        """
        Checks if the area of the current square is < area of another.

        Args:
            other (Square): Another square.

        Returns:
            bool: True if the area is less, False otherwise.
        """
        return (
                self.area() < other.area()
                ) if isinstance(other, Square) else False

    def __le__(self, other):
        """
        Checks if the area of the current square is <= area of another.

        Args:
            other (Square): Another square.

        Returns:
            bool: True if the area is less than or equal, False otherwise.
        """
        return (
                self.area() <= other.area()
                ) if isinstance(other, Square) else False
