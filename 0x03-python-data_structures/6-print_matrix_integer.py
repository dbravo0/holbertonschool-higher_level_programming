#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for line in row:
            if line == row[-1]:
                print(end="{:d}".format(line))
            else:
                print(end="{:d} ".format(line))
        print()
