#!/usr/bin/python3
# 8-rectangle.py
# Matthew Ernst 6628@holbertonstudents.com
"""makes an empty class BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Empty class Rectangle"""
    def __init__(self, width, height):
        """Initilizing the Rectangle"""
        """Need to bring in the integer_validator with new added properties"""
        """Using integer_validator can ensure positive #s"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Finding area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """print() should print, and str() should return
        the following rectangle description: [Rectangle] <width>/<height>"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
    
    def __init__(self, size):
        """class Square that inherits from Rectangle"""
        return(self.__width * self.__height)
