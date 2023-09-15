#!/usr/bin/python3
# 0-add_integer.tpy
# Matthew Ernst <6628@holbertonstudents.com>
""" function to add two integers """


def add_integer(a, b=98):
    """Returns the sum of integers a and b.

    Float arguments will be casted to int before adding.

    Raises:
        TypeError: if a or b are not float or int
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
