#!/usr/bin/python3

def class_to_json(obj):
    """
    Function that returns the dictionary description
    with simple data structure (list, dictionary, string)
    """

    return obj.__dict__
