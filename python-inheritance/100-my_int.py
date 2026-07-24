#!/usr/bin/python3


"""Module providing a custom integer class with inverted comparison logic.

This module defines the MyInt subclass of int, which overrides equality and
inequality operators to return opposite results."""


class MyInt(int):
    """Custom integer class that inverts standard comparison behavior.

    This class inherits from int but reverses the meaning of == & != operators
    It also validates input during initialization to ensure
    only valid integers are accepted, raising a TypeError for
    any other type with a specific message."""

    def __init__(self, value):
        """Initialize a new MyInt instance with strict integer validation.

        This constructor checks if the provided 'value'
        is an int. If not, it raises
        a TypeError with a custom message"""

        if type(value) is not int:
            raise TypeError("int must be an int, dumbass")
        self.value = value

    def __eq__(self, other):
        """Return True when this instance is NOT equal to other.

        This method overrides the standard equality check by
        returning the result of the parent's 'not equals' operator instead,
        effectively inverting logic."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Return True when this instance IS equal to other.

        This method overrides the standard inequality check by
        returning the result of the parent's equality operator instead,
        effectively inverting logic."""
        return super().__eq__(other)
