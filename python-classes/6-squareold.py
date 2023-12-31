#!/usr/bin/python3
# 6-square.py
# Matthew Ernst <6628@holbertonstudents.com>
"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """set the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        msgerr = "position must be a tuple of 2 poisitive integers"
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(v, int) for v in value) or
                any(v < 0 for v in value)):
            raise TypeError(msgerr)
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print square with the #. """
        if self.__size == 0:
            print()
            return

        for i in range(0, self.__position[1]):
            print("")
        for i in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for k in range(0, self.__size):
                print("#", end="")
            print()

    def display(self):
        """Print square with the # to the position. """
        if self.__size == 0:
            print()
            return

        pattern = [
            [" " * self.__position[0] + "#" * self.__size]
            for _ in range(self.__position[1])]

        pattern.extend(
            (" " * self.__position[0] + "#" * self.__size)
            for _ in range(self.__size))

        print("\n".join(pattern))
