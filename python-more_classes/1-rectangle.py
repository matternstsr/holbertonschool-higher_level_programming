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
        """Retrieves the height of the Rectangle"""
        return self.__width
    
    @property
    def height(self):
        """Retrieves the width of the Rectangle"""
        return self.__height
    
    @width.setter
    def width(self, value):
        """Sets the height of the Rectangle"""
        if type(value) == int:
            if value >= 0:
                self.__width = value
            else:
                raise TypeError("width must be an integer")
        else:
            raise ValueError("width must be >= 0")

    @height.setter
    def height(self, value):
        """Sets the width of the Rectangle"""
        if type(value) == int:
            if value >= 0:
                self.__height = value
            else:
                raise TypeError("height must be an integer")
        else:
            raise ValueError("height must be >= 0")
        
"""Traceback (most recent call last):
  File "/home/matternstsr/holbertonschool-higher_level_programming/python-more_classes/./1-main.py", line 2, in <module>
    Rectangle = __import__('1-rectangle').Rectangle
  File "/home/matternstsr/holbertonschool-higher_level_programming/python-more_classes/1-rectangle.py", line 22
    if is not (value, int):
       ^^
SyntaxError: invalid syntax"""
"""Traceback (most recent call last):
  File "/home/matternstsr/holbertonschool-higher_level_programming/python-more_classes/./1-main.py", line 2, in <module>
    Rectangle = __import__('1-rectangle').Rectangle
  File "/home/matternstsr/holbertonschool-higher_level_programming/python-more_classes/1-rectangle.py", line 22
    if is not isinstance(value, int):
       ^^
SyntaxError: invalid syntax"""
"""Traceback (most recent call last):
  File "/home/matternstsr/holbertonschool-higher_level_programming/python-more_classes/./1-main.py", line 2, in <module>
    Rectangle = __import__('1-rectangle').Rectangle
  File "/home/matternstsr/holbertonschool-higher_level_programming/python-more_classes/1-rectangle.py", line 28
    @height.setter
                  ^
IndentationError: unindent does not match any outer indentation level"""
"""Traceback (most recent call last):
  File "/home/matternstsr/holbertonschool-higher_level_programming/python-more_classes/./1-main.py", line 4, in <module>
    my_rectangle = Rectangle(2, 4)
  File "/home/matternstsr/holbertonschool-higher_level_programming/python-more_classes/1-rectangle.py", line 9, in __init__
    self.width = width
  File "/home/matternstsr/holbertonschool-higher_level_programming/python-more_classes/1-rectangle.py", line 26, in width
    self.width = value
  File "/home/matternstsr/holbertonschool-higher_level_programming/python-more_classes/1-rectangle.py", line 26, in width
    self.width = value
  File "/home/matternstsr/holbertonschool-higher_level_programming/python-more_classes/1-rectangle.py", line 26, in width
    self.width = value
  [Previous line repeated 993 more times]
  File "/home/matternstsr/holbertonschool-higher_level_programming/python-more_classes/1-rectangle.py", line 22, in width
    if not isinstance(value, int):
RecursionError: maximum recursion depth exceeded while calling a Python object"""
"""{'_width': 2, '_height': 4}
{'_width': 10, '_height': 3}"""
