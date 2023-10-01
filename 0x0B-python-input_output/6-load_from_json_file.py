#!/usr/bin/python3
from json import loads

"""
A module to load an object from a .json file
"""

def load_from_json_file(filename):
    """
    Function to derive an object from a .json file
    """
    with open(filename, encoding="utf-8", mode="r") as file:
        return loads(file.read())
