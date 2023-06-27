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

    def set_size(self, value):
        if type(value) != int:
            raise Exception("size must be an integer")
        self.__size = value

    def get_size(self):
        return self.__size

    size = property(get_size, set_size)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for i in range(self.__size):
                    print('#', end='')
                print()
