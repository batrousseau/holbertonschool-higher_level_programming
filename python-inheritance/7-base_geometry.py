#!/usr/bin/python3


"""Module providing a base class for geometry-related functionality.

This module defines the BaseGeometry abstract-like class intended to serve as a
foundation for other geometry classes. Currently doesnt implement any specific
geometry logic but provides a common starting point for inheritance."""


class BaseGeometry:
    """Base class for all geometry objects in this package.

    This is an empty base class designed to be subclassed by more specific
    geometry implementations. It serves as the root of the geometry hierarchy
    within this module, allowing common attributes or methods to potentially
    be added later without breaking existing subclasses."""

    def area(self):
        """Calculate and return the area of the geometric shape.

        This method is intended to be implemented by concrete subclasses. Since
        BaseGeometry itself doesnt define a specific geometry logic, it raises
        exception when called directly to indicate that functionality must be
        provided in derived classes.

        Raises:
            Exception: Always raised with message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a given value is an integer greater than zero.

        This method stores the provided 'name' & 'value' as instance attributes
        It acts as a placeholder 4 validation logic which might be expanded in
        subclasses or future versions of this class. No actual type checking or
        error raising occurs in this specific implementation; simply assigns
        values to self.name and self.value.

        Args:
            name (str): The attribute name associated with the value.
            value (int): An integer expected to be greater than zero.
        """
        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError(f"{self.name} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
