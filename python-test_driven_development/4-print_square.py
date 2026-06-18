#!/usr/bin/python3
"""
This modules contains a unique function but is still
worth commenting on in case you need to print a square
"""


def print_square(size):
    """
    print_square - print a square with #character
    size: the number of # that must be printed,
    must be and int and > 0
    Return: Nothing except the pleasure of seeing
    a square in a terminal (and that's something)
    """
    if size is None:
        return
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
