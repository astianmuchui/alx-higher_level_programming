#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for int in list:
            if list.index(int) < (len(list) - 1):
                print("{:d}".format(int), end=" ")
            else:
                print("{:d}".format(int), end="")
        print()
