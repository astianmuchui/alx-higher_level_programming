#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):

    if isinstance(key, str):
        if a_dictionary.get(key):
            a_dictionary[key] = value
        else:
            a_dictionary[key] = value
    else:
        return
