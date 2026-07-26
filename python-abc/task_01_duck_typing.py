#!/usr/bin/python3


from abc import ABC, abstractmethod
import math


"""Module defining geometric shapes using duck typing and inheritance.

This module provides Shape as an abstract base class for
Circle and Rectangle subclasses. It includes utility functions to
compute area and perimeter dynamically based on the object."""


class Shape(ABC):
    """Abstract base class representing any shape with calculable properties.

    This class defines two abstract methods 'area' and 'perimeter'
    that must be implemented by all concrete subclasses like Circle
    or Rectangle, ensuring consistent interface usage."""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """A circle shape inheriting from Shape with
    radius-based calculations.

    This class implements the abstract methods to compute
    area and circumference using pi,
    validating that the radius is an integer or float during initialization."""

    def __init__(self, radius):
        self.radius = radius
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("Radius must be an int or a float")

    def area(self):
        """Calculate and print the circle's area
        using pi times radius squared."""

        self.area = math.pi * self.radius**2
        print(f"Area: {self.area}")

    def perimeter(self):
        """Calculate and print the
        circle's circumference (perimeter)."""

        self.perimeter = 2 * math.pi * self.radius
        print(f"Perimeter: {self.perimeter}")


class Rectangle(Shape):
    """A rectangle shape inheriting from Shape with
    width and height properties.

    This class implements area as product of dimensions and
    perimeter as sum of all sides, using private attributes for
    internal storage and property setters for validation."""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and print the rectangle's area
        as width times height."""

        self.area = self.width * self.height
        print(f"Area: {self.area}")

    def perimeter(self):
        """Calculate and print the rectangle's perimeter
        as sum of all sides."""

        self.perimeter = 2 * (self.width + self.height)
        print(f"Perimeter : {self.perimeter}")


def shape_info(obj):
    """Print area and perimeter info for any
    Shape subclass instance.

    This function validates that the provided object is an
    instance of a class inheriting from Shape,
    then calls its 'area' and 'perimeter' methods to display results."""

    if not isinstance(obj, Shape):
        raise TypeError("Only accept arguments which inherits from Shape")
    obj.area()
    obj.perimeter()
