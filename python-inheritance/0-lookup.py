#!/usr/bin/python3

"""
This module provides a function to inspect the attributes
and methods of an object.
"""


def lookup(obj):

    """
    Returns a list of the attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list containing the names of the
        object's attributes and methods.
    """
    empty: list = dir(obj)
    return (empty)
