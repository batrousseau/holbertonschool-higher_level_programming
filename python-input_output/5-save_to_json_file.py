#!/usr/bin/python3

"""Module providing a utility to save Python objects as JSON files.

This module defines the save_to_json_file function which serializes
any valid Python object into its corresponding JSON string representation
and writes it directly to a file with UTF-8 encoding."""
import json


def save_to_json_file(my_obj, filename):
    """Serialize 'my_obj' to JSON and write to 'filename'.

    Converts provided object using json.dump() then opens
    target file in write mode. Writes serialized data as text
    encoded in utf-8 without returning any value from this
    operation directly."""

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
