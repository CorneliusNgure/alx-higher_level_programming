#!/usr/bin/python3
"""Defines a function that creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """creates an object from JSON
    Args:
        filename (str): the name of the file.
    """
    with open(filename) as a_file:
        return json.load(a_file)
