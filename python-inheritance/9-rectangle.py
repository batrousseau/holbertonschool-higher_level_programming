#!/usr/bin/python3


"""Module providing a Rectangle class inheriting from BaseGeometry.

This module imports the BaseGeometry base class & defines
the Rectangle subclass, which adds width and height attributes
with validation inherited from the parent."""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle shape inheriting validation logic from BaseGeometry.

    This class extends BaseGeometry to represent a 2D rectangular
    area using validated integer dimensions
    for width and height only."""
    def __init__(self, width, height):
        """Initialize a new Rectangle instance with validated dimensions.

        This constructor calls the parent's
        validation methods for both 'width' and 'height'.
        After successful validation it stores these values in internal"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle.

        This method computes the product of the
        private '__width' and '__height' attributes to determine
        the total surface area of the shape."""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the Rectangle instance.

        Returns:
            str: A formatted string '[Rectangle] <width>/<height>'.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
