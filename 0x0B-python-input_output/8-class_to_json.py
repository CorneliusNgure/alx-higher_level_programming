#!/usr/bin/python3
"""Defines dict description of a class"""

import json


def class_to_json(obj):
    """Returns dict description of a class for JSON serialization"""
    return obj.__dict__
