#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) != 0:
        numrows = len(matrix)
        numcolumns = len(matrix[0])
        for rows in range(numrows):
            for columns in range(numcolumns):
                if columns == numcolumns - 1:
                    print('{:d}'.format(matrix[rows][columns]))
                else:
                    print('{:d} '.format(matrix[rows][ccolumns])
    else:
        print()
