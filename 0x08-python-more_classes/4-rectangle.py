#!/usr/bin/python3

''' An Empty class to define a rectangle '''


class Rectangle:
    ''' Empty class that defines a rectangle '''

    def __init__(self, width=0, height=0):
        ''' Constructor method '''
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def __str__(self):
        ''' Returns a # representation of the rectangle
        To be used with print() and str() built-in
        functions'''

        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return (("#" * self.__width + "\n") * self.__height)[:-1]

    def __repr__(self):
        """
        return a string representation of the rectangle
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    @property
    def width(self):
        ''' Property getter for width private instance attribute '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' Property setter for width private instance attribute '''
        if isinstance(value, int):
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        ''' Property getter for height private instance attribute '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' Property setter for height private instance attribute '''
        if isinstance(value, int):
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    def area(self):
        ''' A public instance Method that returns the area of the rectangle '''
        return self.__width * self.__height

    def perimeter(self):
        ''' A public instance Method that should return
        the perimeter of the rectangle '''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    pass
