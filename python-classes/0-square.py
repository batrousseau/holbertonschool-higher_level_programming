#!/usr/bin/python3
"""Square module.

This module provides a simple definition of a Square class
for basic geometric manipulations.
"""


class Square:
    """Represents a square geometric shape."""

    def __init__(self, side: int):
        """Initialize a new instance of the Square class.

        Args:
            side (int, float): The length of a side of the square.
        """
        self.side: int = side
