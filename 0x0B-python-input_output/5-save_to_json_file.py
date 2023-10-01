#!/usr/bin/python3
import json

"""
A module to write an Obj to a file, using a JSON notation
"""


def save_to_json_file(my_obj, filename):
    """
     A function to write an Obj to a file, using a JSON notation
    """
    with open(filename, encoding="utf-8", mode="w") as file:
        file.write(json.dumps(my_obj))
