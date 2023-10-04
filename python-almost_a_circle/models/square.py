#!/usr/bin/python3
""" Module for the Square Class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class representing a square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes a Square instance

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square.
            y (int): The y-coordinate of the square.
            id (int): The identifier of the square.

        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter for the size of the square """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for the size of the square """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """ Returns a string representation of the square """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """ Updates the attributes of the square """
        if args:
            if len(args) >= 1:
                if args[0] is not None:
                    self.id = args[0]
                else:
                    self.__init__(self.size, self.x, self.y)
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is not None:
                        self.id = value
                    else:
                        self.__init__(self.size, self.x, self.y)
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """ Returns the dictionary representation of a square """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
