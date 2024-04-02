#!/usr/bin/python3
""" 2D matrix rotation module. """


def rotate_2d_matrix(matrix):
    """ Rotates an m by n 2D matrix in place."""
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    for i in range(n):
        matrix[i] = matrix[i][::-1]
