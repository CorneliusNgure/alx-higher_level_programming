#!/usr/bin/python3
"""Subclass of the built-in, int"""


class MyInt(int):
    """Inverts the equal and not equal signs"""
    def __eq__(self, value):
        """Inverts the == sign"""
        return super().__ne__(value)

    def __ne__(self, value):
        """Inverts the != sign"""
        return super().__eq__(value)
