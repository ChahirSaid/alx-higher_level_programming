#!/usr/bin/python3
"""
Module 0-add_integer
Defines an integer addition function.
"""


def add_integer(a, b=98):
    """
    Returns a + b as int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
