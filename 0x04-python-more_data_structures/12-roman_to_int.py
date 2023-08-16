#!/usr/bin/python3
def roman_to_int(roman_string):

    if not roman_string or type(roman_string) is not str:
        return 0

    if "IV" in roman_string:
        roman_string = roman_string.replace("IV", "4")

    elif "IX" in roman_string:
        roman_string = roman_string.replace("IX", "9")

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

        elif int(i):
            sum += int(i)

        else:
            return 0
    return sum
