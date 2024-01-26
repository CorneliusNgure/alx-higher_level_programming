#!/usr/bin/python3
"""Defines a write-object-to-text-file function using JSON"""
import json


def save_to_json_file(my_obj, filename):
    """Writes object to text file using JSON representation

    Args:
        my_obj (str): The object.
        filename (str): The file.
    """
    with open(filename, mode="w", encoding="utf-8") as a_file:
        json.dump(my_obj, a_file)
