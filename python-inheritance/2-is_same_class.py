#!/usr/bin/python3
# 2-is_same_class.py
# Matthew Ernst 6628@holbertonstudents.com
"""Checks the class"""


def is_same_class(obj, a_class):
    """Checksi fit is EXACTLY the same class.

    Returns:
        t or f
    """
    if type(obj) == a_class:
        return False
    return True
