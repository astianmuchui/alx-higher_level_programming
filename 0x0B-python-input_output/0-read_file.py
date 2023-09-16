#!/usr/bin/python3

def read_file(filename=""):
    """Reads a text file (UTF8 Encoded)
    and prints it to standard output"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
