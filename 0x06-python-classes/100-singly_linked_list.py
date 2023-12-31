#!/usr/bin/python3
"""Defines a class Node and a class SinglyLinkedList."""


class Node:
    """Represents a node in a singly linked list."""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""
    def __init__(self):
        self.__head = None

    def __str__(self):
        nodes = []
        current = self.__head
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        new = Node(value)
        if not self.__head:
            self.__head = new
            return
        if value < self.__head.data:
            new.next_node = self.__head
            self.__head = new
            return
        current = self.__head
        while current.next_node and value > current.next_node.data:
            current = current.next_node
        new.next_node = current.next_node
        current.next_node = new
