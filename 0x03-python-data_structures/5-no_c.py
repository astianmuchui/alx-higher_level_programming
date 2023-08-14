#!/usr/bin/python3
def no_c(my_string):
    arr = [x for x in my_string if x != 'c' and x != 'C']
    strcpy = ""
    for i in arr:
        strcpy += i
    return strcpy
