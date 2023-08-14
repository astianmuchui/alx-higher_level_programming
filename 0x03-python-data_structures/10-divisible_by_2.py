#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    divs = [x for x in my_list if x % 2 == 0]
    undivs = [x for x in my_list if x % 2 != 0]

    for i in divs:
        my_list[my_list.index(i)] = True

    for i in undivs:
        my_list[my_list.index(i)] = False

    return my_list
