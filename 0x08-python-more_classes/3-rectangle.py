#!/usr/bin/python3
"""Module representing the blueprint of Rectangle class"""


class Rectangle:
    """Defines the Rectangle class"""

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class

        Args:
            width (int): width of a rectangle
            height (int): height of a rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets and sets the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets and sets the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """mod string object"""
        if self.height == 0 or self.width == 0:
            return ""
        return ('\n'.join("#" * self.width for i in range(self.height)))
