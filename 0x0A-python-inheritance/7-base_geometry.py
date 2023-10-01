#!/usr/bin/python3

"""Create a class `BaseGeometry`"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(value))
    pass
