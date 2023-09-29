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

    def __str__(self):
        """Returns the print() and str() representation of the Square."""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}")

"""10. And now, the Square!
Write the class Square that inherits from Rectangle:

In the file models/square.py
Class Square inherits from Rectangle
Class constructor: def __init__(self, size, x=0, y=0, id=None)::
Call the super class with id, x, y, width and height - this super call will
use the logic of the __init__ of the Rectangle class. The width and height
must be assigned to the value of size
You must not create new attributes for this class, use all attributes of
Rectangle - As reminder: a Square is a Rectangle with the same width and
height
All width, height, x and y validation must inherit from Rectangle - same
behavior in case of wrong data
The overloading __str__ method should return [Square] (<id>) <x>/<y> - <size>
- in our case, width or height
As you know, a Square is a special Rectangle, so it makes sense this class 
Square inherits from Rectangle. Now you have a Square class who has the same
attributes and same methods."""