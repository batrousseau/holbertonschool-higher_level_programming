#!/usr/bin/python3

"""Square module.

This module provides a simple definition of a Square class
for basic geometric manipulations.
"""


class Square:
    """Represents a square geometric shape."""

    def __init__(self, size=0):
        """Initialize a new instance of the Square class."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """ Compute the area of the square"""

    def area(self):
        area: int = self.__size ** 2
        return (area)
