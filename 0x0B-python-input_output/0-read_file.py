#!/usr/bin/python3
"""Defines a function that prints text file to stdout"""


def read_file(filename=""):
    """Reads a UTF8 text file"""
    with open(filename, encoding="utf8", mode="r") as a_file:
        print(a_file.read(), end="")
