#!/usr/bin/python3


'''class MyList that inherits from list obj'''


class MyList(list):
    """class MyList that inherits from list obj"""
    def print_sorted(self):
        """prints the list, but in sorted (ascending sort) format """
        print(sorted(self))
