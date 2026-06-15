#!/usr/bin/python3

"""
This module contains a fonction that print a name,
or at least two strings
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name - Prints two strings
    first_name: a string
    last_name: a string
    Return: Nothing
    """

    if first_name is None:
        raise TypeError("first_name must be a string")
    if last_name is None:
        raise TypeError("last_name must be a string")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    max_string_size = 10 * 10 * 1024
    if len(first_name) > max_string_size or len(last_name) > max_string_size:
        raise ValueError("Too much text in variables")
    print(f"My name is {first_name} {last_name}")
