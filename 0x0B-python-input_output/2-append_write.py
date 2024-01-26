#!/usr/bin/python3
"""Defines a function that appends at the eof"""


def append_write(filename="", text=""):
    """Appends a string at the end of file

    Args:
        filename (str): Name of the file
        text (str): Text to be apppended.
    Returns: The number of chars appended.
    """
    with open(filename, mode="a", encoding="utf-8") as a_file:
        return a_file.write(text)
