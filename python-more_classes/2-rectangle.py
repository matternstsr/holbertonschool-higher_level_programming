#!/usr/bin/python3
# 1-rectangle.py
# Matt Ernst
""" class Rectangle that defines a rectangle0-rectangle.py  ". """


class Rectangle:
    """Define new class"""
    def __init__(self, width=0, height=0):
        """Initialize new class rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the height of the Rectangle"""
        return self.__width

    @property
    def height(self):
        """Retrieves the width of the Rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the height of the Rectangle"""
        if type(value) == int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, value):
        """Sets the width of the Rectangle"""
        if type(value) == int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
