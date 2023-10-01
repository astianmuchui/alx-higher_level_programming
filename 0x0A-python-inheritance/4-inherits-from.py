#!/usr/bin/python3

"""
returns True if the object is an instance of a class that inherited
(directly or indirectly) from the specified class ; otherwise False
 """


def inherits_from(obj, a_class):
    """Will Check if an object is an instance of
    a class that inherited from, the specified class"""

    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
