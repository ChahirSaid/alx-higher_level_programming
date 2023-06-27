#!/usr/bin/python3
class Square:
    __size = None
    __position = None

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        if type(size) != int:
            raise Exception("size must be an integer")
        if size < 0:
            raise Exception("size must be >= 0")
        if (type(position[0]) != int or type(position[1]) != int):
            raise Exception("position must be a tuple of 2 positive integers")
        if len(position) != 2 or type(position) != tuple:
            raise Exception("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise Exception("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        return (self.__size * self.__size)

    def set_size(self, value):
        if type(value) != int:
            raise Exception("size must be an integer")
        self.__size = value

    def get_size(self):
        return self.__size

    size = property(get_size, set_size)

    def set_position(self, value):
        if (type(value[0]) != int or type(value[1]) != int):
            raise Exception("position must be a tuple of 2 positive integers")
        if len(value) != 2 or type(value) != tuple:
            raise Exception("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise Exception("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def get_position(self):
        return self.__position

    position = property(get_position, set_position)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(' ', end='')
                for i in range(self.__size):
                    print('#', end='')
                print()
