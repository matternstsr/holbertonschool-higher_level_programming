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

In the code you provided, the with statement is used to open the file 
specified by the filename parameter and read its contents using the utf-8 
encoding. The with statement automatically closes the file after its 
contents have been read .

You don’t need to manage file permission or file doesn’t exist exceptions 
because the open() function will raise an exception if it fails to open the 
file ."""

def read_file(filename=""):
    """defines read file"""
    with open(filename, encoding="utf-8") as DaFile:
        print(DaFile.read(), end="")
