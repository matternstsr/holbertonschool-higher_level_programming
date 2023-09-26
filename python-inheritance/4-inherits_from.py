#!/usr/bin/python3
# 3-is_same_class.py
# Matthew Ernst 6628@holbertonstudents.com
"""Checks the class"""


def is_kind_of_class(obj, a_class):
    """Checks if it is inhertited or instance same class.

    Returns:
        t or f
    """
    if isinstance(obj, a_class):
        return True
    return False