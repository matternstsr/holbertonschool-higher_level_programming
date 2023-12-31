#!/usr/bin/python3
# rectangle.py
# Matthew Ernst 6628@holbertonstudents.com
"""Makes a Base Class"""
from models.base import Base


class Rectangle(Base):
    """New Class Base"""
    typeer = " must be an integer"
    valer = " must be > 0"

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
        if value <= 0:
            raise ValueError("x" + self.valer)
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
        if value <= 0:
            raise ValueError("y" + self.valer)
        self.__y = value

    @property
    def id(self):
        """Getter for id"""
        return self.__id

    @id.setter
    def id(self, value):
        """Setter for id"""
        if type(value) is not int:
            raise TypeError("id" + self.typeer)
        if value <= 0:
            raise ValueError("id" + self.valer)
        self.__id = value
        
        
"""1. Base class
Write the first class Base:

Create a folder named models with an empty file __init__.py inside -
with this file, the folder will become a Python package

Create a file named models/base.py:

Class Base:
private class attribute __nb_objects = 0
class constructor: def __init__(self, id=None)::
if id is not None, assign the public instance attribute id with this
argument value - you can assume id is an integer and you don’t need to test
the type of it
otherwise, increment __nb_objects and assign the new value to the public
instance attribute id
This class will be the “base” of all other classes in this project.
The goal of it is to manage id attribute in all your future classes
and to avoid duplicating the same code (by extension, same bugs)
        
        
        
2. First Rectangle
Write the class Rectangle that inherits from Base:

In the file models/rectangle.py
Class Rectangle inherits from Base
Private instance attributes, each with its own public getter and setter:
__width -> width
__height -> height
__x -> x
__y -> y
Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
Call the super class with id - this super call with use the logic of 
the __init__ of the Base class
Assign each argument width, height, x and y to the right attribute
Why private attributes with getter/setter? Why not directly public attribute?

Because we want to protect attributes of our class. With a setter,
you are able to validate what a developer is trying to assign to a variable.
So after, in your class you can “trust” these attributes.

"""