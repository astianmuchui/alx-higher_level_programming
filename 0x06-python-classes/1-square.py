#!/usr/bin/python3

''' An Empty class to define a square '''


class Square:
    ''' Empty class to define a square and its size attribute'''

    def __init__(self, size):
        ''' Size is a private instance attribute for class square,
        The size of a square is crucial for the square, many things
        depend of it(area computation, etc.),
        so you, as class builder, must control the type and value of
        this attribute. One way to have the control is to keep it privately.'''
        self.__size = size
    pass
