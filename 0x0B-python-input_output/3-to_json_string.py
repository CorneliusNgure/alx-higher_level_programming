#!/usr/bin/python3
"""Defines function to return JSON representation of an ob    ject string"""

import json


def to_json_string(my_obj):
    """Returns a JSON string

    Args:
        my_obj (str): object string.
    Return:
        JSON representation of my_obj string.
    """
    return json.dumps(my_obj)
