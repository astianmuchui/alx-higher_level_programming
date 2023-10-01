#!/usr/bin/python3
"""
Class student that defines a student by
first name, last name and age
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """sinple class that defines a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary representation of a student"""
        return self.__dict__
