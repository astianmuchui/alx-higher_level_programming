#!/usr/bin/bash

def safe_print_list_integers(my_list=[], x=0):

    j = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                j += 1
            else:
                pass
    except Exception:
        pass

    print()
    return (j)
