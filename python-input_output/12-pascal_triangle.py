#!/usr/bin/python3
"""Module for Pascal"""


def pascal_triangle(n):
    """Function is documented"""

    if n <= 0:
        return []

    if n == 1:
        return list(1)

    res = [[1], [1, 1]]

    if n == 2:
        return res

    for row in range(1, n-1):
        prev_row = res[row]
        new_row = [1]
        for n in range(len(prev_row)-1):
            new_row.append(prev_row[n] + prev_row[n+1])
        new_row.append(1)
        res.append(new_row)
    return res
