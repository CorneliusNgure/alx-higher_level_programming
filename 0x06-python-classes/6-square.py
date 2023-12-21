#!/usr/bin/python3

"""
    module defines the Square class of square with size and position.

    Classes:
        Square: Represents a square with size and position.
"""


class Square:
    """
    Square class represents a square.

    Attributes:
    - size (int): Size of the square.
    - position (tuple): Position of the square in the format (x, y).

    Methods:
    - __init__(self, size=0, position=(0, 0)): init instance of Square class.
    - size(self): Getter method for retrieving the size attribute.
    - size(self, value): Setter method for setting the size attribute.
    - position(self): Getter method for retrieving the position attribute.
    - position(self, value): Setter method for setting the position attribute.
    - area(self): Computes and returns the area of the square.
    - my_print(self): Prints the square using '#' with optional position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (int): Size of the square (default is 0).
        - position (tuple): Position of the square. Default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for retrieving the size attribute.

        Returns:
        int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size attribute.

        Parameters:
        value (int): The size value to set.

        Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method for retrieving the position attribute.

        Returns:
        tuple: The position of the square in the format (x, y).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for setting the position attribute.

        Parameters:
        value (tuple): The position value to set.

        Raises:
        TypeError: If the position is not a tuple of two positive integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(i, int) for i in value)
            or not all(i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' character with optional position.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
