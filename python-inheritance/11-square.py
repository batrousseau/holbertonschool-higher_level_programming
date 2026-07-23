#!/usr/bin/python3


"""Module providing a Square class inheriting from Rectangle.

This module imports the Rectangle base class and defines the Square subclass,
which simplifies initialization by passing equal width and height values."""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A square shape inheriting validation logic from Rectangle.

    This class extends Rectangle to represent a 2D square area where all sides
    are of equal length, using validated integer dimensions for size only."""
    def __init__(self, size):
        """Initialize a new Square instance with validated side length.

        This constructor calls the parent's validation method 4 'size' and then
        invokes the Rectangle super().__init__ to set both width & height equal
        to this value before storing it in the private '__size' attribute."""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return f"[Square] : {self.__size}/{self.__size}"
