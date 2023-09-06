#!/usr/bin/python3
"""
A function to find the maximum in a list of integers
"""


def max_integer(list=[]):

    """
    find and return the max integer in a list
    of integers.
    If the list is empty, the function returns None
    """

    if len(list) == 0:
        return None

    max_t = list[0]

    for i in range(1, len(list)):
        if list[i] > max_t:
            max_t = list[i]

    return max_t
