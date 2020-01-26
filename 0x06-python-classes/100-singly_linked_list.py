#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            new_n = Node(value)
            new_n.next_node = self.__head
            self.__head = new_n

        else:
            new_n = Node(value)
            new_n.data = value
            new_n.next_node = self.__head
            self.__head = new_n

    def __str__(self):
        current = self.__head
        n_list = []
        while current is not None:
            n_list.append(str(current.data))
            current = current.next_node
        n_list.sort(key=int)
        return ("\n".join(n_list))

