#!/usr/bin/python3
# 1-rectangle.py
# Matt Ernst
""" class Rectangle that defines a rectangle0-rectangle.py  ". """


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        
    @property
    def width(self):
        return self.width
    
    @property
    def height(self):
        return self.height
    
    @width.setter
    def width(self, value):
        if is not (value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.width = value

     @height.setter
    def height(self, value):
        if is not (value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.height = value

"""Traceback (most recent call last):
  File "/home/matternstsr/holbertonschool-higher_level_programming/python-more_classes/./1-main.py", line 2, in <module>
    Rectangle = __import__('1-rectangle').Rectangle
  File "/home/matternstsr/holbertonschool-higher_level_programming/python-more_classes/1-rectangle.py", line 22
    if is not (value, int):
       ^^
SyntaxError: invalid syntax"""
