#!/usr/bin/python3

def print_last_digit(number):

    if isinstance(number, int):
        last_dig = abs(number) % 10

    if number == 0:
        last_dig = 0

    print(last_dig, end="")
    return last_dig
