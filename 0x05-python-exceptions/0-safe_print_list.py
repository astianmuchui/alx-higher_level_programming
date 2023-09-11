#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        val = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            val += 1
        print()
        return val
    except Exception:
        print()
        pass
