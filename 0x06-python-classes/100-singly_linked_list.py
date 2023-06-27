#!/usr/bin/python3
class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:

    def __init__(self):
        self.__head = None

    def __str__(self):
        string = ""
        temp = self.__head

        while temp is not None:
            string += str(temp.data)
            temp = temp.next_node
            if temp is not None:
                string += "\n"
        return string

    def sorted_insert(self, value):

        new = Node(value)
        if self.__head is None:
            self.__head = new
            return

        temp = self.__head

        if new.data < temp.data:
            new.next_node = self.__head
            self.__head = new
            return

        while temp.next_node is not None and new.data > temp.next_node.data:
            temp = temp.next_node
        new.next_node = temp.next_node
        temp.next_node = new
        return
