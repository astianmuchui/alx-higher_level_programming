#!/usr/bin/python3

"""Create a subclass of BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""Class Rectangle that inherits from base geometry"""


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Instantiation with width and height private inst attrs"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
