#!/usr/bin/python3
import json
"""
A module to load an object from a .json file
"""


def load_from_json_file(filename):
    """
    Function to derive an object from a .json file
    """
    with open(filename, encoding="utf-8", mode="r") as file:
        return json.loads(file.read())
