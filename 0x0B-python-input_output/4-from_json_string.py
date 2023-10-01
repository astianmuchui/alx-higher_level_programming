#!/usr/bin/python3
"""
A module to stringify a JSON object
"""


from json import loads


def from_json_string(my_str):
    """
        A function to stringify a JSON object
    """
    return loads(my_str)
