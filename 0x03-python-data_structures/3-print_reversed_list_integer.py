#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    max_idx = len(my_list) - 1
    for n in my_list:
        print("{:d}".format(my_list[max_idx]))
        max_idx -= 1
