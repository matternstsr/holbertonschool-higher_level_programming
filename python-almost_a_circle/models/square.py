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
            print(f"{'' * self.x}")
        for _ in range(self.height):
            print(f"{' ' * self.x}{ '#' * self.width}")

    def __str__(self):
        """Returns the print() and str() representation of the Square."""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}")

    def update(self, *args, **kwargs):
        """Returns the argument(s) selected or if no args then all"""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
        if args is None:
            return (f"[Square] ({self.id}) {self.x}/{self.y} - "
                    f"{self.width}")
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
