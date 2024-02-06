#!/usr/bin/python3
"""Pascal's Triangle Generator"""


def pascal_triangle(n):
    """Generate Pascal's Triangle up to n rows"""
    if n <= 0:
        return []

    triangle = [[1]]

    for row_nbr in range(1, n):
        row = [1]
        for col_index in range(1, row_nbr):
            element = triangle[row_nbr - 1][col_index - 1] + triangle[row_nbr - 1][col_index]
            row.append(element)
        row.append(1)
        triangle.append(row)

    return triangle
