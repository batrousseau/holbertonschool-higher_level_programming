#!/usr/bin/python3


"""Module providing a utility function to check class identity.

This module defines the is_same_class function which verifies if an object's
type matches exactly with a provided class, without considering inheritance.
It returns True only when obj is an instance of a_class and not derived from it
"""


def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of the given class.

    This function compares the type of 'obj' directly with 'a_class'. It does
    not consider inheritance hierarchies; therefore, instances of subclasses
    will return False even if they inherit from 'a_class'. Returns True only
    when 'obj' is strictly an instance of 'a_class'.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if type(obj) == a_class, False otherwise.
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class must be a class")
    if type(obj) is a_class:
        return (True)
    return (False)
