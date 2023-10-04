#!/usr/bin/python3
# square.py
# Matthew Ernst 6628@holbertonstudents.com
"""Makes a Square Class"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Initializes Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes Square Class with new attributes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def display(self):
        """Prints a representation of a Square using "#"."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Returns the print() and str() representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Updates Square attributes based on arguments or keyword arguments"""
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for i in range(len(args)):
                if i < len(attrs) and args[i] is not None:
                    setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in attrs and value is not None:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Defines a dictionary representation for a Square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
