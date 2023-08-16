#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    new = [x for x in set_1 if x in set_1 and x not in set_2]
    new_2 = [x for x in set_2 if x in set_2 and x not in set_1]
    return set(new + new_2)
