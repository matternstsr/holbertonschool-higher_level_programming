#!/usr/bin/python3
# File: 11-student.py
# Matthew Ernst 6628@holbertonstudents.com
"""Defines and student class"""


class Student:
    """Student class defined"""

    def __init__(self, first_name, last_name, age):
        """attribs defined for the class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """all in list or all"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """Load all attributes of the student and sort key value pairs."""
        for kvp, value in json.items():
            setattr(self, kvp, value)
