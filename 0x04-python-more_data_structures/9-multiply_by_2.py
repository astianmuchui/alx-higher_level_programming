#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    keys = [x for x in a_dictionary.keys()]
    values = [(x*2) for x in a_dictionary.values()]

    for i in range(0, len(a_dictionary)):
        a_dictionary[keys[i]] = values[i]
    return a_dictionary
