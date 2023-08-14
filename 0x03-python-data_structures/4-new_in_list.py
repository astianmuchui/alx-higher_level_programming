#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_cpy = my_list[:]
    if idx > 0 and idx < len(my_list) and my_list is not None:
        x = my_list[idx]
        list_cpy[idx] = element
        return list_cpy
    else:
        return my_list[:]
