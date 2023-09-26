#!/usr/bin/python3
# 7-is_same_class.py
# Matthew Ernst 6628@holbertonstudents.com
"""makes an empty class BaseGeometry"""


class BaseGeometry:
    """ Empty class BaseGeometry"""
    def area(self):
        """returns the area if implimented"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """that validates value"""
        if (value) is not int:
            raise Exception ("{} must be an integer".format(name))
        if value <= 0:
            raise Exception ("{} must be greater than 0".format(name))
