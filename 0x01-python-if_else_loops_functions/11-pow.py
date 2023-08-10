#!/usr/bin/python3

def pow(a, b):

    res = 1

    if b == 0:
        res = 1

    elif b == 1:
        res = a

    else:
        for i in range(b + 1):
            res *= a
    return res
