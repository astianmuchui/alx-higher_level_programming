#!/usr/bin/python3

def uppercase(str):

    new = ""
    for i in str:

        if ord(i) not in range(97, 123):
            new += i
        else:
            hex_val = 26 - (123 - ord(i))
            new_val = 65 + hex_val

            new += chr(new_val)

    print("{}".format(new))
