#!/usr/bin/python3
class Square:
    __size = None

    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise Exception("size must be an integer")
        if size < 0:
            raise Exception("size must be >= 0")

    def area(self):
        return (self.__size * self.__size)
