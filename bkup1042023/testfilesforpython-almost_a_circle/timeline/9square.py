#!/usr/bin/python3
# square.py
# Matthew Ernst 6628@holbertonstudents.com
"""Makes a Square Class"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes Base Class with new attributes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if type(value) is not int:
            raise TypeError("size" + self.typeer)
        if value <= 0:
            raise ValueError("size" + self.valer)
        self.__size = value
"""9. Update #1
mandatory
Score: 12.20% (Checks completed: 12.20%)
Update the class Rectangle by updating the public method def
update(self, *args): by changing the prototype to
update(self, *args, **kwargs) that assigns a key/value
argument to attributes:

**kwargs can be thought of as a double pointer to a dictionary: key/value
As Python doesn’t have pointers, **kwargs is not literally a double
pointer – describing it as such is just a way of explaining its
behavior in terms you’re already familiar with
**kwargs must be skipped if *args exists and is not empty
Each key in this dictionary represents an attribute to the instance
This type of argument is called a “key-worded argument”. Argument order is
not important."""