#!/usr/bin/python3
"""class Student that defines a student by"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Function that retuns the dictionary description of an obj"""
        return self.__dict__
