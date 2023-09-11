#!/usr/bin/python3

''' An Empty class to define a square '''


class Square:

    ''' Empty class to define a square and its size attribute'''

    def __init__(self, size=0):

        ''' Size is a private instance attribute for class square,
        The size of a square is crucial for the square, many things
        depend of it(area computation, etc.),
        so you, as class builder, must control the type and value of
        this attribute. One way to have the control is to keep it privately.'''

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        ''' Public instance method that returns the area, in essence size^2 '''
        return (self.__size ** 2)
    pass
