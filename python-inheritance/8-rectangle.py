#!/usr/bin/python3
# 8-rectangle.py
# Matthew Ernst 6628@holbertonstudents.com
"""makes an empty class BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Empty class Rectangle"""
    def __init__(self, width, height):
        """Initilizing the Rectangle"""
        """Need to bring in the integer_validator with new added properties"""
        """Using integer_validator can ensure positive #s"""
        
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
