#!/usr/bin/python3

"""Module providing a utility to convert JSON strings
back into Python objects.

This module defines the from_json_string function which
uses the standard library's json.loads() method to deserialize
any valid JSON string representation of a Python object
(dict, list, str, int, float, bool, None) back into its original form."""
import json


def from_json_string(my_str):
    """Deserialize 'my_str' from a JSON formatted string.

    Uses json.loads() from the standard library to parse
    and convert the provided valid JSON string into the corresponding
    Python object structure or raises TypeError if parsing fails due to
    invalid syntax or unsupported types within the data."""

    return json.loads(my_str)
