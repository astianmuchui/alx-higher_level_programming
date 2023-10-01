#!/usr/bin/python3
from json import loads

"""
A module to stringify a JSON object
"""


def from_json_string(my_str):
    """
        A function to stringify a JSON object
    """
    return loads(my_str)
