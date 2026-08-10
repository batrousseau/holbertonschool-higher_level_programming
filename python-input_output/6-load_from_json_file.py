#!/usr/bin/python3

"""Module providing a utility to load Python objects from JSON files.

This module defines the load_from_json_file function which reads a file,
parses its content as valid JSON and returns the corresponding deserialized
Python object."""
import json


def load_from_json_file(filename):
    """Load and deserialize 'filename' into a Python object.

    Opens target file in read mode with utf-8 encoding.
    Uses json.load() to parse contents and return resulting object
    or raises exception if invalid JSON found."""

    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
