#!/usr/bin/python3
# base.py
# Matthew Ernst 6628@holbertonstudents.com
"""Makes a Base Class"""
from models.base import Base


class Rectangle(Base):
    """New Class Base"""
    typeer = " must be an integer"
    valer = " must be > 0"

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes Base Class with new attributes"""
        self.width = width
        self.width = height
        self.x = x
        self.y = y
        self.id = id
        super().__init__(id)

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter for Width"""
        if type(width) is not int:
            raise TypeError("width" + self.typeer) 
        if width <= 0:
            raise ValueError("width" + self.valer)
        self.__width = width

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter for x"""
        if type(x) is not int:
            raise TypeError("x" + self.typeer) 
        if x <= 0:
            raise ValueError("x" + self.valer)
        self.__x = x

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @x.setter
    def y(self, y):
        """Setter for y"""
        if type(y) is not int:
            raise TypeError("y" + self.typeer) 
        if y <= 0:
            raise ValueError("y" + self.valer)
        self.__y = y

    @property
    def id(self):
        """Getter for id"""
        return self.__id

    @id.setter
    def id(self, id):
        """Setter for id"""
        if type(id) is not int:
            raise TypeError("id" + self.typeer) 
        if id <= 0:
            raise ValueError("id" + self.valer)
        self.__id = id
