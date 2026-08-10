#!/usr/bin/python3

"""Module providing a utility to convert Python objects into JSON strings.

This module defines the to_json_string function which uses
the standard library's json.dumps() method to serialize any valid Python object
(dict, list, str, int, float, bool, None) into its corresponding
JSON string representation."""

import json


def to_json_string(my_obj):
    """Convert 'my_obj' to a JSON formatted string.

    Uses json.dumps() from the standard library to serialize
    the provided object. Returns the resulting JSON string or raises TypeError
    if serialization fails due to unsupported
    types within the object structure."""

    return json.dumps(my_obj)
