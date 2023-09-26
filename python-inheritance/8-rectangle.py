#!/usr/bin/python3
# 8-rectangle.py
# Matthew Ernst 6628@holbertonstudents.com
"""makes an empty class BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Empty class Rectangle"""
    def __init__(self, width, height):
        """Initilizing the Rectangle"""
