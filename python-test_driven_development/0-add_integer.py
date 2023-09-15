#!/usr/bin/python3
# 0-add_integer.tpy
# Matthew Ernst <6628@holbertonstudents.com>
"""Adds two integers: """


def add_integer(a, b=98):
    """adds two inegers"""
    if (a is None or not isinstance(a, int) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if (b is None or not isinstance(b, int) and (not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
    #pass