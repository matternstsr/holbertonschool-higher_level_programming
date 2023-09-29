#!/usr/bin/python3
# rectangle.py
# Matthew Ernst 6628@holbertonstudents.com
"""Makes a Base Class"""
from models.base import Base


class Rectangle(Base):
    """New Rectangle Class"""
    typeer = " must be an integer"
    valer = " must be > 0"
    axiserr = " must be >= 0"
    column = 0
    row = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes Base Class with new attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        """self.id = id old dont work"""
        super().__init__(id)

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for Width"""
        if type(value) is not int:
            raise TypeError("width" + self.typeer)
        if value <= 0:
            raise ValueError("width" + self.valer)
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if type(value) is not int:
            raise TypeError("height" + self.typeer)
        if value <= 0:
            raise ValueError("height" + self.valer)
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        if type(value) is not int:
            raise TypeError("x" + self.typeer)
        if value < 0:
            raise ValueError("x" + self.axiserr)
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        if type(value) is not int:
            raise TypeError("y" + self.typeer)
        if value < 0:
            raise ValueError("y" + self.axiserr)
        self.__y = value

    def area(self):
        """returns the area of a given rectangle"""
        return self.height * self.width

    def display(self):
        """Prints a representation of a rectangle using "#"."""
        for _ in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """Returns the print() and str() representation of the rectangle."""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}")
"""6. __str__
Update the class Rectangle by overriding the __str__
method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
"""Finding the indentation and the structure of the string was hard,
ended up finding a way to shorten my display method by half.
I way over think things :)"""