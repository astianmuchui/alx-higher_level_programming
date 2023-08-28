#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        result = 0
        for i in range(x + 1):
            if isinstance(my_list[i], int):
                print("{:d}".format(i), end="")
                result += 1
            else:
                pass
        print()
        return result
    except Exception:
        pass
