#!/usr/bin/python3


"""Module providing a utility to append
text content into files safely.

This module defines the append_write function which opens
any file in append mode with UTF-8 encoding, writes provided text
data inside it and returns the number of characters written."""


def append_write(filename="", text=""):
    """Append 'text' to 'filename' and return bytes
    appended.

    Opens or creates a file named 'filename', encodes content as UTF-8
    in append mode, writes exactly 'text' into it using context manager for
    safe resource handling, then returns the count of
    characters successfully written."""

    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
