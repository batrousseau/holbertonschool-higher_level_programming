#!/usr/bin/python3


"""Module providing a utility to read and print file contents safely.

This module defines the read_file function which opens any text
file with UTF-8 encoding,
reads its entire content into memory, and prints it directly
to standard output."""


def read_file(filename=""):
    """Read and print the contents of 'filename' using
    UTF-8 encoding.

    Opens the specified file (defaulting to empty string if
    none provided), reads all data,
    then prints it immediately without storing in a
    variable beyond the context manager scope."""

    with open(filename, encoding="utf-8") as f:
        print(f"{f.read()}")
