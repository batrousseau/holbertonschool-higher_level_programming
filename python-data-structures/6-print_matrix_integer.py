#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 and not matrix[0]:
        print()
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (j < len(matrix[0]) - 1):
                    print("{:d}".format(matrix[i][j]), end=" ")
                else:
                    print("{:d}".format(matrix[i][j]))
