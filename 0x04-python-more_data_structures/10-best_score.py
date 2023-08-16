#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        if isinstance(max(a_dictionary, key=a_dictionary.get), int):
            return max(a_dictionary, key=a_dictionary.get)
        else:
            return None
    else:
        return None
