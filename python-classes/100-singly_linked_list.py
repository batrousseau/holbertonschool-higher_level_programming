#!/usr/bin/python3

class Node():

    def __init__(self, data=int(), next_node=None):
        self.data: int = data
        self.next_node = next_node

    @property
    def data(self):
        return (self.__data)

    @property
    def next_node(self):
        return (self.__next_node)

    @data.setter
    def data(self, data):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data

    @next_node.setter
    def next_node(self, next_node):
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node


class SinglyLinkedList():
    def __init__(self):
        self.__head = None
        self.__count: int = 0

    def __str__(self):
        node_temp = self.__head
        to_print: str = ""
        while node_temp.next_node is not None:
            to_print = to_print + str(node_temp.data) + "\n"
            node_temp = node_temp.next_node
            self.__count += 1
        if node_temp.next_node is None:
            to_print = to_print + str(node_temp.data)
        return f"{to_print}"

    def sorted_insert(self, value):
        """I need to have the head and a pointer to move"""
        node_ptr: Node = None
        nn: Node = Node(value)

        """ I need to handle case where there is no head"""
        if self.__head is None:
            self.__head = nn
            return
        """I need to handle the case where the new node became the head"""
        if self.__head.data > nn.data:
            node_ptr = self.__head
            self.__head = nn
            nn.next_node = node_ptr
            return
        """I need to handle classical case & when my new node is the last"""
        node_ptr = self.__head
        while (node_ptr.next_node is not None):
            if node_ptr.data <= nn.data and nn.data < node_ptr.next_node.data:
                nn.next_node = node_ptr.next_node
                node_ptr.next_node = nn
                return
            node_ptr = node_ptr.next_node

        if node_ptr.next_node is None:
            node_ptr.next_node = nn
