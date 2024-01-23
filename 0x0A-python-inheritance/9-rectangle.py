#!/usr/bin/python3
"""Defines Rectangle class that inherits form BaseGeometry"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Subclass of the BaseGeometry class"""

    def __init__(self, width, height):
        """Initializes a new rectangle
        Args:
            width (int): Width of the rectangle.
            height (int): height of the rectangle.
    """
        BaseGeometry.__init__(self)

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the str representation of the rectangle"""
        class_name = self.__class__.__name__
        return "[{}] {}/{}".format(class_name, self.__width, self.__height)
