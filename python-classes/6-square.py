#!/usr/bin/python3
# 6-square.py
# Matthew Ernst <6628@holbertonstudents.com>
"""Define a class Square."""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
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
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(v, int) for v in value) or
            any(v < 0 for v in value)
        ):
            raise TypeError("position must be a tuple of two positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
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
        if self.__size == 0:
            print()
            return

        pattern = [
            [" " * self.__position[0] + "#" * self.__size]
            for _ in range(self.__position[1])
        ]

        pattern.extend([" " * self.__position[0] + "#" * self.__size for _ in range(self.__size)])

        print("\n".join(pattern))

