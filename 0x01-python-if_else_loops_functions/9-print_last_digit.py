#!/usr/bin/python3

def print_last_digit(number):

    if isinstance(number, int):
        last_dig = abs(number % 10)
    return last_dig
