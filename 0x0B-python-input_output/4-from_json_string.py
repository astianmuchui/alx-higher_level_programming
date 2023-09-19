#!/usr/bin/python3
import json


def from_json_string(my_str):
    """
        A function to stringify a JSON object
    """
    return json.loads(my_str)
