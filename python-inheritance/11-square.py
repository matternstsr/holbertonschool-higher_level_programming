#!/usr/bin/python3
# 11-rectangle.py
# Matthew Ernst 6628@holbertonstudents.com
"""makes a rectangle BaseGeometry"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square with equal height, equal width"""

    def __init__(self, size):
        """Initializes new Square"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
        
    def __str__(self):
        """It's a square now"""
        return '[Square] {}/{}'.format(self.__size, self.__size)
