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

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes Base Class with new attributes"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        """self.id = id old dont work"""
        super().__init__(id)

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @width.setter
    def width(self, value):
        """Setter for Width"""
        if type(value) is not int:
            raise TypeError("width" + self.typeer)
        if value <= 0:
            raise ValueError("width" + self.valer)
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter for height"""
        if type(value) is not int:
            raise TypeError("height" + str(self.typeer))
        if value <= 0:
            raise ValueError("height" + self.valer)
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter for x"""
        if type(value) is not int:
            raise TypeError("x" + self.typeer)
        if value < 0:
            raise ValueError("x" + self.axiserr)
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter for y"""
        if type(value) is not int:
            raise TypeError("y" + self.typeer)
        if value < 0:
            raise ValueError("y" + self.axiserr)
        self.__y = value

    """@property
    def id(self):
        return self.__id
    @id.setter
    def id(self, value):
        if type(value) is not int:
            raise TypeError("id" + self.typeer)
        if value < 0:
            raise ValueError("id" + self.valer)
        self.__id = value"""
