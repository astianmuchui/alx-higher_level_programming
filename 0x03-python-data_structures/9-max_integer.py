#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) != 0:
        max = 0
        for n in my_list:
            if n > max:
                max = n
        return max
    else:
        return None
