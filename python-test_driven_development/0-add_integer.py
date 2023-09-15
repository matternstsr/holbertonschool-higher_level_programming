#!/usr/bin/python3
# 0-add_integer.tpy
# Matthew Ernst <6628@holbertonstudents.com>
"""Adds two integers: """


def add_integer(a, b=98):
    """adds two inegers"""
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
