#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        print()
        return [[item**3 for item in row] for row in matrix]
