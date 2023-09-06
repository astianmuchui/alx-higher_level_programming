#!/usr/bin/python3

"""
Prints `My name is <first name> <last name>`
"""


def say_my_name(first_name, last_name=""):
    """
    first_name and last_name must be strings else,
    raise a TypeError exception
    (first_name must be a string or
    last_name must be a string)
    """

    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")

    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
