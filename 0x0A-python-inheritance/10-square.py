#!/usr/bin/python3
"""Create a subclass of Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Instantiation with size private inst attr"""

        self.integer_validator("size", size)
        self.__size = size

    def area(self):

        return self.__size ** 2
