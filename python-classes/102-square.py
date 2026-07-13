#!/usr/bin/python3

"""Square module.

This module provides a simple definition of a Square class
for basic geometric manipulations.
"""


class Square:
    """Represents a square geometric shape."""

    def __init__(self, size=0):
        """
        Initializes the Square instance with an optional size attribute.

        :param size: The side length of the square.
        Defaults to 0 if not provided.
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieves the current size of the square.

        :return: The size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, size):
        """
        Sets the size of the square to a given value.

        :param size: The new size for the square.
        Must be an integer greater than or equal to 0.
        :raises TypeError: If the size is not an integer.
        :raises ValueError: If the size is negative.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """ Compute the area of the square"""

    def area(self):
        area: int = self.__size ** 2
        return (area)

    def __eq__(self, other):
        """
        Checks if two Square instances are equal based on their size.

        :param other: Another Square instance to compare with.
        :return: True if the sizes are equal, False otherwise.
        """
        if self.__size == other.__size:
            return True

    def __ne__(self, other):
        """
        Checks if two Square instances are not equal based on their size.

        :param other: Another Square instance to compare with.
        :return: True if the sizes are not equal, False otherwise.
        """
        if self.__size != other.__size:
            return True

    def __lt__(self, other):
        """
        Checks if this Square is less than another Square based on their size.

        :param other: Another Square instance to compare with.
        :return: True if this Square's size is less than the other
        Square's size, False otherwise.
        """
        if self.__size < other.__size:
            return True

    def __le__(self, other):
        """
        Checks if this Square is less than or equal to another
        Square based on their size.

        :param other: Another Square instance to compare with.
        :return: True if this Square's size is less than or equal
        to the other Square's size, False otherwise.
        """
        if self.__size <= other.__size:
            return True

    def __gt__(self, other):
        """
        Checks if this Square is greater than another
        Square based on their size.

        :param other: Another Square instance to compare with.
        :return: True if this Square's size is greater
        than the other Square's size,
        False otherwise.
        """
        if self.__size > other.__size:
            return True

    def __ge__(self, other):
        if self.__size >= other.__size:
            return True
