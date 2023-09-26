#!/usr/bin/python3
# 1-my_list.py
# Matthew Ernst 6628@holbertonstudents.com
"""Write a function that reads a text file (UTF8)
(Unicode Transformation Format - 8 bits) and prints it to stdout:
Prototype: def read_file(filename=""):
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.
You are not allowed to import any module"""

"""The with statement in Python is used to wrap the execution of a block of
code with methods defined by a context manager. In the case of file I/O
operations, it provides a way to ensure that a file is closed when the block
inside the with statement is exited, regardless of how the block is exited .

The with statement is used to open the file
specified by the filename parameter and read its contents using the utf-8
encoding. The with statement automatically closes the file after its
contents have been read .

You don’t need to manage file permission or file doesn’t exist exceptions
because the open() function will raise an exception if it fails to open the
file ."""
"""Open file and return a stream. Raise OSError upon failure.

file is either a text or byte string giving the name (and the path if the
file isn't in the current working directory) of the file to be opened or an
integer file descriptor of the file to be wrapped. (If a file descriptor is
given, it is closed when the returned I/O object is closed, unless closefd
is set to False.)"""


def read_file(filename=""):
    """defines read file"""
    with open(filename, 'r', encoding="utf-8") as DaFile:
        print(DaFile.read(), end="")
