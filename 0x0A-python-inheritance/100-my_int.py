#!/usr/bin/python3

"""
a class MyInt that inherits from int:

MyInt is a rebel. MyInt has == and != operators inverted

"""


class MyInt(int):

    """MyInt class"""
    def __eq__(self, other):
        """equals method"""
        return super().__ne__(other)

    def __ne__(self, other):
        """not equal method"""
        return super().__eq__(other)
