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
            if args[0] is not None:
                self.id = args[0]
            else:
                self.__init__(self.size, self.x, self.y)
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is not None:
                        self.id = value
                    else:
                        self.__init__(self.size, self.x, self.y)
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """ defines a dictionary for a Square from rectangle"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
            }

14. Square instance to dictionary representation
Update the class Square by adding the public method def to_dictionary(self):
that returns the dictionary representation of a Square:
This dictionary must contain:
id
size
x
y