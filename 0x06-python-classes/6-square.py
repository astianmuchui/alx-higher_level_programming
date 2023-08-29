#!/usr/bin/python3

''' An Empty class to define a square '''


class Square:

    ''' Empty class to define a square and its size attribute'''

    def __init__(self, size=0, position=(0, 0)):

        ''' Size is a private instance attribute for class square,
        The size of a square is crucial for the square, many things
        depend of it(area computation, etc.),
        so you, as class builder, must control the type and value of
        this attribute. One way to have the control is to keep it privately.'''

        self.__size = size
        self.__position = position

    def area(self):
        ''' Public instance method that returns the area, in essence size^2 '''
        return (self.__size ** 2)

    @property
    def size(self):
        ''' Public instance method to return the size  '''
        return self.__size

    @size.setter
    def size(self, value):
        ''' Public instance method to set the size  '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        ''' Public instance method to return the position '''
        return self.__position

    @position.setter
    def position(self, value):
        ''' Public instance method to set the position '''
        if not isinstance(value, tuple) or len(value) != 2 or \
           not isinstance(value[0], int) or not isinstance(value[1], int) \
           or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        ''' Public instance method to print the square using character # '''
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
    pass
