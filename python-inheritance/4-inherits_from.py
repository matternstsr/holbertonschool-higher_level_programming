#!/usr/bin/python3
# 3-is_same_class.py
# Matthew Ernst 6628@holbertonstudents.com
"""Checks the class"""


def inherits_from(obj, a_class):
    """Sub class to sub class"""
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return False
    else:
        return False