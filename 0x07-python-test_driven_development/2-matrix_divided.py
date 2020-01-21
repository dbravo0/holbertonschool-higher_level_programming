#!/usr/bin/python3

def matrix_divided(matrix, div):
    matrix_clone = [[]]
    x = 0
    y = 0
    if matrix is None:
        raise TypeError("Matrix must be a matrix of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("Matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix[0]) == 0:
        raise TypeError("Matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(matrix[x][y], (int, float)):
        raise TypeError("Matrix must be a matrix (list of lists) of integers/floats")
    elif not all(len(x) == len(matrix[0]) for x in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    matrix_clone = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return matrix_clone
