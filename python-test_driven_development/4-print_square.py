#!/usr/bin/python3
"""Prints a square: """


def print_square(size):
    """Prints a square"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    for j in range(size):
        for i in range(size):
            print("#", end="")
        print("")
    