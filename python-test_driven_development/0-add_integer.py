#!/usr/bin/python3


"""
add_integer - function that sums two integers or float
a: first integer or float
b: second integer or float, 98 by default
Return: sum of a and b
"""


def add_integer(a, b=98) -> int:
    """
    Adds two integers.

    >>> add_integer(1, 2)
    3
    >>> add_integer(-5, 10)
    5
    >>> add_integer("hello", 2)
    Traceback (most recent call last):
    TypeError: a must be an integer
    """

    if a is None:
        raise TypeError("a must be an integer")
    if b is None:
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    sum: int = a + b
    return (sum)
