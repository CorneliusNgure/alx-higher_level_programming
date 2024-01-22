#!/usr/bin/python3
"""Module defines base geometry class"""


class BaseGeometry:
    """Represents base geometry"""

    def area(self):
        """Not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate a parameter as an int

        Args:
            name (str): Name of the parameter
            value (int): The parameter to be validated.
        Raises:
            TypeError: If value is not an int.
            ValueError: If value <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
