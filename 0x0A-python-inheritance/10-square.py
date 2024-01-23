#!/usr/bin/python3
"""Defines Square class that inherits from Rectangle"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Subclass of the Rectangle class"""
    def __init__(self, size):
        """Initiate Square
        Args:
            size (int): The size of the Square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
