#!/usr/bin/python3
# File: 11-student.py
# Matthew Ernst 6628@holbertonstudents.com
"""returns a list of lists of integers repr the Pascal’s triangle of n"""


def pascal_triangle(n):
    """Defines a triangle"""
    
    if n <= 0:
        return []
    """Returns empty list if less or equal"""

    triangle = [[1]]
    for current in range(1, n):
        row = [1]
        previous_row = triangle[current - 1]
        for i in range(1, current):
            row.append(previous_row[i] + previous_row[i - 1])
        row.append(1)
        triangle.append(row)

    return triangle