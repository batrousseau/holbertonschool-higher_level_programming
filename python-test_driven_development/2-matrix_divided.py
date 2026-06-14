#!/usr/bin/python3

"""
This module provides matrix manipulation utilities.

It contains a single function, `matrix_divided`, which performs element-wise
division on a 2D matrix (list of lists) containing integers or floats.
The module validates input shapes, type consistency, and prevents division
by zero errors by raising appropriate exceptions (TypeError, ZeroDivisionError).
"""

def matrix_divided(matrix, div):
    """
    matrix-divided : divide each value of the matrix
    by the number div
    matrix: matrix of integer or float
    div: divider for each value of the matrix
    Return: new matrix divided
    """
    if not matrix and not matrix[0]:
        return (None)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    matrix_row_lenghts: list = []
    for k in range(len(matrix)):
        try:
            matrix_row_lenghts.append(len(matrix[k]))
        except TypeError:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    set_row: set = set(matrix_row_lenghts)
    if len(set_row) > 1:
        raise IndexError("Each row of the matrix must have the same size")

    new_matrix: list = []
    for i in range(len(matrix)):
        new_row: list = []
        for j in range(len(matrix[i])):
            try:
                division = matrix[i][j] / div
                new_row.append(round(division, 2))
            except TypeError:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            except ZeroDivisionError:
                raise ZeroDivisionError("division by zero")
        new_matrix.append(new_row)
    return (new_matrix)
