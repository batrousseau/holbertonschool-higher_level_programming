#!/usr/bin/python3


"""Module providing a utility to extract object attributes as dictionary.

This module defines the class_to_json function which retrieves
instance __dict__ and returns it directly without modification."""


def class_to_json(obj):
    """Extract all public attributes of 'obj' into a dictionary.

    Uses obj.__dict__ to access internal state representation for
    serialization purposes only in this context flow path here."""

    dict_obj = obj.__dict__
    return dict_obj
