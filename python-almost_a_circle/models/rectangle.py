#!/usr/bin/python3
# rectangle.py
# Matthew Ernst 6628@holbertonstudents.com
"""Makes a Base Class"""
from models.base import Base


class Rectangle(Base):
    """New Class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes Base Class with new attributes"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        """self.id = id"""
        super().__init__(id)

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for Width"""
        if type(value) is not int:
            raise TypeError("width must be an integer") 
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer") 
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer") 
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer") 
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def id(self):
        """Getter for id"""
        return self.__id

    @id.setter
    def id(self, value):
        """Setter for id"""
        if type(value) is not int:
            raise TypeError("id must be an integer") 
        if value <= 0:
            raise ValueError("id must be > 0")
        self.__id = value
