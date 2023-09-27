#!/usr/bin/python3
# 10-class_to_json.py
# Matthew Ernst 6628@holbertonstudents.com
"""Write a class Student that defines a student by: (based on 9-student.py)
Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age:
def __init__(self, first_name, last_name, age):
Public method def to_json(self, attrs=None):
that retrieves a dictionary representation of a Student instance
(same as 8-class_to_json.py):
If attrs is a list of strings, only attribute names contained
in this list must be retrieved.
Otherwise, all attributes must be retrieved
You are not allowed to import any module"""


class Student:
    """its a student"""

    def __init__(self, first_name, last_name, age):
        """initalize a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


def to_json(self, attrs=None):
    if attrs is None:
        return self.__dict__
    else:
        return {attr: getattr(self, attr) for attr in attrs}
