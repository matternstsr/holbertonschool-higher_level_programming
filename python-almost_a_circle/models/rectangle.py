#!/usr/bin/python3
""" Module for the Rectangle Class """
from models.base import Base


class Rectangle(Base):
    """ Class representing a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes a Rectangle instance

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle.
            y (int): The y-coordinate of the rectangle.
            id (int): The identifier of the rectangle.

        """
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("width and height must be integers")
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for the width of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for the height of the rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter for the x-coordinate of the rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for the x-coordinate of the rectangle """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter for the y-coordinate of the rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for the y-coordinate of the rectangle """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of the rectangle """
        return self.width * self.height

    def display(self):
        """ Prints a representation of the rectangle using "#" """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """ Returns a string representation of the rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ Updates the attributes of the rectangle """
        if args:
            if len(args) >= 1:
                if args[0] is not None:
                    self.id = args[0]
                else:
                    self.__init__(self.width, self.height, self.x, self.y)
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is not None:
                        self.id = value
                    else:
                        self.__init__(self.width, self.height, self.x, self.y)
                if key == 'width':
                    self.width = value
                if key == 'height':
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """ Returns the dictionary representation of a rectangle """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
