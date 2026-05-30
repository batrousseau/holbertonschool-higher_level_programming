#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix and not matrix[0]:
        return (None)
    new_matrix: list = []
    for i in range(len(matrix)):
        new_matrix.append(list(map(lambda x: x * x, matrix[i])))
    return (new_matrix)
