#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        new_row = list([a**2 for a in i])
        new_matrix.append(new_row)
    return new_matrix
