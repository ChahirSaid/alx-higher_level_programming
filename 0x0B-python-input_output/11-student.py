#!/usr/bin/python3
"""class Student that defines a student by"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Function that retuns the dictionary description of an obj"""

        if (type(attrs) == list and
                all(type(e) == str for e in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for a in json:
            self.__dict__[a] = json[a]
