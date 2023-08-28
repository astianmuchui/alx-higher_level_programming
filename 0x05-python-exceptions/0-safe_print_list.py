#!usr/bin/python3

def safe_print_list(my_list=[], x=0):
    new = []

    try:
        for i in range(x):
            new.append(my_list[i])
            print(my_list[i], end="")
    except IndexError:
        pass
    finally:
        print()
        return x
