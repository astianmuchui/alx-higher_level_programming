#!/usr/bin/python3

"""
A module to write a string to a text file (UTF8) and returns the number
of characters written to the file
"""


def write_file(filename="", text=""):
    """
        Writes a string to a text file (UTF8) and returns the number
        of characters written to the file
    """
    with open(filename, encoding="utf-8", mode="w") as file:
        return file.write(text)
