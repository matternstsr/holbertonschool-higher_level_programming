#!/usr/bin/python3
# 4-is_same_class.py
# Matthew Ernst 6628@holbertonstudents.com
"""Checks the class"""


def inherits_from(obj, a_class):
    """Sub class to sub class"""
    if issubclass(type(obj), a_class):
        if type(obj) != a_class:
            return True
    return False
