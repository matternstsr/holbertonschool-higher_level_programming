#!/usr/bin/python3
# square.py
# Matthew Ernst 6628@holbertonstudents.com
"""Makes a Square Class"""
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
        self.__size = value

    def __str__(self):
        """Returns the print() and str() representation of the Square."""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}")
