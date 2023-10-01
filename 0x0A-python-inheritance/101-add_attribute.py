#!/usr/bin/python3

"""
a function that adds a new attribute to an object if its possible:
Raise a TypeError exception, with the message can't add new attribute
if the object cant have new attribute
You are not allowed to use try/except
"""


def add_attribute(obj, name, value):

    """adds a new attribute to an object if its possible"""
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
