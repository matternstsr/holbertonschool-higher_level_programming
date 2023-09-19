#!/usr/bin/python3
# 1-rectangle.py
# Matt Ernst
""" class Rectangle that defines a rectangle0-rectangle.py  ". """


class Rectangle:
    """Define new class"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize new class rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, value):
        """Sets the width of the Rectangle"""
        if type(value) == int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """define area"""
        return self.__width * self.__height

    def perimeter(self):
        """define perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """Return the rectagle using #."""
        if self.__width == 0 or self.__height == 0:
            return ("")
        pattern = []
        for i in range(self.__height):
            for j in range(self.__width):
                pattern.append('#')
            if i is not self.__height - 1:
                pattern.append("\n")
        return ("".join(pattern))

    def bigger_or_equal(rect_1, rect_2):
        """Finds the bigger rectangle based on area.

        Args:
            rect_1 compares first
            rect_2 compares second
        Raises:
            TypeError: If neither are Rectangle.
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """ Creates a new Rectangle (square) with equal w and h.

        Args:
            size (int): width and height values.
        """
        return (cls(size, size))

    def __repr__(self):
        """String rep of rec"""
        return "Rectangle({}, {})".format(str(self.width), str(self.height))

    def __del__(self):
        """Deletes the class rectangle cool but weird"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
