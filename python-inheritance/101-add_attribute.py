#!/usr/bin/python3


"""Module providing a utility to add attributes dynamically.

This module defines the add_attribute function which attempts
to set a new attribute on an object if it is mutable and does not
already possess that attribute."""


def add_attribute(obj, name, value):
    """Add a new attribute 'name' with given 'value' to 'obj'.

    This function checks if 'obj' allows dynamic attributes.
    It raises TypeError if the object type (str, int, tuple) forbids
    it or if the attribute already exists."""

    if obj not in globals():
        raise TypeError("can't add new attribute")
    if hasattr(obj, name):
        raise TypeError("can't add new attribute")
    if type(obj) is str or type(obj) is int or type(obj) is tuple:
        raise TypeError("can't add new attribute")
    obj.name = value
