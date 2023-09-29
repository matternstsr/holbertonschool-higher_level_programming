#!/usr/bin/python3
# rectangle.py
# Matthew Ernst 6628@holbertonstudents.com
"""Makes a Base Class"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes Base Class with new attributes"""
        super().__init__(size, size, x, y, id)
        
    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if type(value) is not int:
            raise TypeError("size" + self.typeer)
        if value <= 0:
            raise ValueError("size" + self.valer)
        self.__size = value