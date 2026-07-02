#!/usr/bin/python3

"""Square module.

This module provides a simple definition of a Square class
for basic geometric manipulations.
"""


class Square:
    """Represents a square geometric shape."""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """ Compute the area of the square"""

    def area(self):
        area: int = self.__size ** 2
        return (area)

    """Print the square as #"""
    def my_print(self):
        if self.__size == 0:
            print()
        for lenght in range(self.__size):
            for height in range(self.__size):
                print("#", end="")
            print()
