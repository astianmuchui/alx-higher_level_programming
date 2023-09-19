#!/usr/bin/python3

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
