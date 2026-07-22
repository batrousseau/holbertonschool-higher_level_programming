#!/usr/bin/python3


"""Module providing a utility function to check class inheritance hierarchy.

This module defines inherits_from function which verifies if an object's type
is derived from a specified class using issubclass(). It ensures that 'a_class'
is valid type before performing checks & distinguishes between direct instances
and subclasses of the given class.
"""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a subclass of the given class.

    This function verifies whether 'obj' is derived from 'a_class'. It uses
    issubclass() to check inheritance hierarchy and ensures that 'obj' is not
    directly an instance of 'a_class', meaning it must be a proper subclass.
    A TypeError is raised if 'a_class' is not a valid Python class/type object.

    Args:
        obj (any): The object to check for subclass status.
        a_class (type): The base class against which the type should be checked

    Returns:
        bool: True if obj is an instance of a subclass of a_class, False othw.

    Raises:
        TypeError: If 'a_class' is not a valid Python class/type object.
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class must be a class")
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return (True)
    return (False)
