#!/usr/bin/python3

def append_write(filename="", text=""):
    """
    Appends a string to a text file (UTF8) and returns the number
    of characters appended
    """
    with open(filename, encoding="utf-8", mode="a") as file:
        return file.write(text)
