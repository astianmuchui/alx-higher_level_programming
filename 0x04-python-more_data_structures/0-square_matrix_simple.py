#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    nested = []
    final = []

    for lis_t in matrix:
        nested = [pow(x, 2) for x in lis_t]
        final.append(nested)

    return final
