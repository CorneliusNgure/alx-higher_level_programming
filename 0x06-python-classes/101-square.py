#!/usr/bin/python3

"""
    Module defines Square class of a square with size and position.

Classes:
- Square: Represents a square with size and position.

"""


class Square:
    """
    Square class representing a square with size and position.

    Attributes:
    - size (int): Size of the square.
    - position (tuple): Position of the square.

    Methods:
    - area(): Returns the area of the square.
    - my_print(): Prints the square with the character #.
    - __str__(): Returns a string representation of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (int): Size of the square (default is 0).
        - position (tuple): Position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Parameters:
        - value (int): New size value.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Parameters:
        - value (tuple): New position value.

        Raises:
        - TypeError: If position is not a tuple of two positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) for i in value) or \
                not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #."""
        print(str(self))

    def __str__(self):
        """Return a string representation of the square."""
        result = ""
        if self.__size == 0:
            return result

        for _ in range(self.__position[1]):
            result += "\n"

        for _ in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size
            if _ < self.__size - 1:
                result += "\n"

        return result
