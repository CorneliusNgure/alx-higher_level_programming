#!/usr/bin/python3
"""Defines a functin that writes to a text file"""


def write_file(filename="", text=""):
    """Writes to a file and returns the no. of chars written.

    Args:
        filename (str): Name of the file.
        text (str): Text to be written.
    Return:
        The number of characters written.
    """
    with open(filename, encoding="utf-8", mode="w") as a_file:
        return a_file.write(text)
        
