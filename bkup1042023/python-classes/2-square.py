#!/usr/bin/python3
# 2-square.py
# Matthew Ernst <6628@holbertonstudents.com>
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            """Elvaluates if it is an (instance) int
        and if NOT values true due to the not."""
            raise TypeError("size must be an integer")
        elif size < 0:
            """checks to see if size is bigger than or equal to 0."""
            raise ValueError("size must be >= 0")
        self.__size = size
        """sets the size of the square ."""
