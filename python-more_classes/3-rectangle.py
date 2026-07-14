#!/usr/bin/python3

"""
Rectangle class definition.

This Python script defines a simple rectangle class with basic properties and
methods for geometric calculations.
"""


class Rectangle:
    """
    A basic representation of a rectangle in a 2D plane.
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """The length of the rectangle's sides."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The height of the rectangle's sides."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        :return: A string representing the rectangle.
        If the height or width is 0, returns an empty string.
        """
        if self.__height == 0 or self.__width == 0:
            return ("")
        to_print: str = ""
        count: int = 0
        for lenght in range(self.__height):
            for width in range(self.__width):
                to_print = to_print + "#"
            count = count + 1
            if count < self.__height:
                to_print = to_print + "\n"
        return (to_print)

    def area(self):
        """
        Calculate and return the area of the rectangle.

        :return: The area of the rectangle.
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        :return: The perimeter of the rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__height * 2) + (self.__width * 2))
