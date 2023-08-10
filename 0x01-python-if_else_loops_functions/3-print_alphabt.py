#!/usr/bin/python3
for val in range(97, 123):
    if chr(val) != 'q' and chr(val) != 'e':
        print("{0}".format(chr(val)), end="")
