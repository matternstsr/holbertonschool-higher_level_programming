#!/usr/bin/python3
# 8-rectangle.py
# Matthew Ernst 6628@holbertonstudents.com
"""makes an empty class BaseGeometry"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits Rectangle"""
    def __init__(self, size):
        """Initializes an object of Square"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Finding area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """print() should print, and str() should return
        the following rectangle description: [Rectangle] <width>/<height>"""
        return "[Square] {}/{}".format(self.__width, self.__height)
