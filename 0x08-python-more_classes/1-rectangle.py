#!/usr/bin/python3
"""Rectangle class."""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """ Create new Rectangle
        Args:
            width: the width of the new Rectangle
            height: the height of the new Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val < 0:
            raise ValueError("height must be >= 0")
        self.__height = val
