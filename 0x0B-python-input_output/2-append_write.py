#!/usr/bin/python3

"""
A module to append a string to a text file (UTF8) and returns the number
of characters appended
"""


def append_write(filename="", text=""):
    """
    Appends a string to a text file (UTF8) and returns the number
    of characters appended
    """
    with open(filename, encoding="utf-8", mode="a") as file:
        return file.write(text)
