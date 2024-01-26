#!/usr/bin/python3
import json

"""Defines a functin that returns JSON representation of an object string"""


def to_json_string(my_obj):
    """Returns a JSON string

    Args:
        my_obj (str): object string.
    Return:
        JSON representation of my_obj string.
    """
    return json.dumps(my_obj)
