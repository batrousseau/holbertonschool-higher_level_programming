#!/usr/bin/python3


"""Module providing a utility function to check class inheritance.

This module defines the is_kind_of_class function which verifies if an object's
type matches or inherits from a provided class using isinstance(). It includes
validation to ensure that 'a_class' is actually a type before performing checks
"""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of the given class (including subclasses).

    This function verifies whether 'obj' is an instance of 'a_class'. Unlike
    direct type checking, this method considers inheritance hierarchies; thus,
    instances of subclasses will return True. It raises TypeError if 'a_class'
    is not a valid Python class/type object.

    Args:
        obj (any): The object to check for instance status.
        a_class (type): The class against which the type should be checked.

    Returns:
        bool: True if obj is an instance of a_class, False otherwise.

    Raises:
        TypeError: If 'a_class' is not a valid Python class/type object.
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class must be a class")
    if isinstance(obj, a_class):
        return (True)
    return (False)
