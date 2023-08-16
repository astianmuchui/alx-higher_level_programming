#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keys = [x for x in sorted(a_dictionary)]
    dict_t = {}

    for i in keys:
        dict_t[i] = a_dictionary[i]
        print("{}: {}".format(i, a_dictionary[i]))
