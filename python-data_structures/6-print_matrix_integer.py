#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for n in matrix:
        row = []
        for nn in n:
            row.append(nn)
        print(" ".join("{:d}".format(x) for x in row))
