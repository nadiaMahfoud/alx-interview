#!/usr/bin/python3
"""Pascal's Triangle Generator"""


def pascal_triangle(n):
    """Generate Pascal's Triangle up to n rows"""
    if n <= 0:
        return []

    tri = [[1]]

    for row_nbr in range(1, n):
        row = [1]
        for col_ndx in range(1, row_nbr):
            element = tri[row_nbr - 1][col_ndx - 1] + tri[row_nbr - 1][col_ndx]
            row.append(element)
        row.append(1)
        tri.append(row)

    return tri
