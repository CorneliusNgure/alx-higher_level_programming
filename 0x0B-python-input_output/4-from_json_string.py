#!/usr/bin/python3
"""Defines a function that dumps an object to JSON"""
import json


def from_json_string(my_str):
    """Returns a JSON str from a .py data struct object

    Args:
        my_str (str): The string object
    Return:
        JSON string
    """
    return json.dumps(my_str)
