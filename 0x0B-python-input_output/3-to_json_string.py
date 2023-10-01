#!/usr/bin/python3
import json

"""
A module to return the JSON representation of an object (string)
"""


def to_json_string(my_obj):
    """
    Function that returns the JSON notation of a string
    """
    return json.dumps(my_obj)
