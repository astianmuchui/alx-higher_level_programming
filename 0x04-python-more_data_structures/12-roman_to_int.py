#!/usr/bin/python3

def roman_to_int(roman_string):

    if not roman_string or isinstance(roman_string, str) is False:
        return None

    param_t = [x.upper() for x in roman_string]

    dict_t = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    sum = 0
    for i in param_t:
        if dict_t.get(i):
            sum += dict_t.get(i)
        else:
            return None
    return sum
