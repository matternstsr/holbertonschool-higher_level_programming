#!/usr/bin/python3
# 11-rectangle.py
# Matthew Ernst 6628@holbertonstudents.com
"""makes a rectangle BaseGeometry"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits Rectangle"""

    def __init__(self, size):
        """Initializes new Square"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
