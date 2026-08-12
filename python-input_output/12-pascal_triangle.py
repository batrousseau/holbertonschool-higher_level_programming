#!/usr/bin/python3


"""Module providing a utility to generate Pascal's
triangle rows dynamically.

This module defines the pascal_triangle function which
constructs and returns a list of lists representing each
row up to 'n' levels using integer arithmetic."""


def pascal_triangle(n):
    """Generate a list of lists representing
    Pascal's triangle with n rows.

    Returns an empty list if n is less than or
    equal zero. Otherwise builds each row by summing
    adjacent values from the previous row, handling edge
    cases where elements are always one."""

    triangle: list = list()
    if n <= 0:
        return triangle

    for i in range(n):
        row: list = []
        for j in range(i + 1):
            if j == 0 or i == j:
                row.append(1)
            else:
                try:
                    row.append(triangle[i - 1][j] + triangle[i - 1][j - 1])
                except IndexError:
                    row.append(1)
        triangle.append(row)
    return (triangle)
