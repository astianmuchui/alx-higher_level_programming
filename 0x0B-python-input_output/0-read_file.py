#!/usr/bin/python3

"""
A module to read a text file and print it to the stdout
"""


def read_file(filename=""):
    """
     A Function that reads a text file (UTF8) and prints it to the stdout
    """

    """
        By default, print will use stdout as the destination stream.
    """
    with open(filename, encoding="utf-8", mode="r") as file:
        content = file.read()
        print(content, end="")
