#!/usr/bin/python3


"""Module providing a utility to write text content into files safely.

This module defines the write_file function which opens any file in write
mode with UTF-8 encoding, writes provided text data inside it and returns
the number of characters written."""


def write_file(filename="", text=""):
    """Write 'text' to 'filename' and return bytes written.

    Opens or creates a file named 'filename', encodes content
    as UTF-8, writes exactly 'text' into it using context manager
    for safe resource handling, then returns the count of characters
    successfully written."""

    with open(filename, mode="w", encoding="utf-8") as f:
        return (f.write(text))
