#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row = []
    for n in matrix:
        for nn in n:
            row.append(nn)
        print(" ".join(row))    
