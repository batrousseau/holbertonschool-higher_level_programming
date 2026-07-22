#!/usr/bin/python3


"""Module providing a Rectangle class inheriting from BaseGeometry.

This module imports BaseGeometry base class & defines the Rectangle subclass,
which adds width & height attributes with validation inherited frm the parent.
It serves for implementing geometry-specific logic through inheritance."""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle shape inheriting validation logic from BaseGeometry.

    This class extends BaseGeometry to represent a 2D rectangle. It uses
    inherited integer_validator to ensure width and height are valid int
    greater than zero before storing them as private attributes."""

    def __init__(self, width, height):
        """Initialize a new Rectangle instance with validated dimensions.

        This constructor calls the parent's validation methods 4 both 'width' &
        'height'. After successful validation, stores these values in internal
        attributes '__width' and 'height' (private), adhering to existing
        naming conventions without modification of logic or variable names.

        Args:
            width (int): positive integer representing the rectangle's width.
            height (int): positive integer representing the rectangle's height.

        Raises:
            TypeError: If 'width' or 'height' are not integers.
            ValueError: If either dimension is less than or equal to zero.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
