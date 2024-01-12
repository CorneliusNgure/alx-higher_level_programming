#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent instantiation of any object not named "first_name
    """

    __slots__ = ["first_name"]
