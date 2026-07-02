#!/usr/bin/python3

"""Square module.

This module provides a simple definition of a Square class
for basic geometric manipulations.
"""


class Square:
    """Represents a square geometric shape."""

    def __init__(self, size=0, position=(0, 0)):
        self.size: int = size
        self.position: tuple = position

    @property
    def size(self):
        return (self.__size)

    @property
    def position(self):
        return (self.__position)

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @position.setter
    def position(self, position):
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise ValueError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = position

    """ Compute the area of the square"""

    def area(self):
        area: int = self.__size ** 2
        return (area)

    """Print the square as #"""
    def my_print(self):
        if self.__size == 0:
            print()
        for lenght in range(self.__size):
            for pos in range(self.__position[0]):
                print(" ", end="")
            for height in range(self.__size):
                print("#", end="")
            print()
