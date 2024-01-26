#!/usr/bin/python3
"""Defines a JSON-to-string function"""
import json


def from_json_string(my_str):
    """Returns a .py data struct object from JSON

    Args:
        my_str (str): The string object
    Return:
        JSON string
    """
    return json.loads(my_str)
