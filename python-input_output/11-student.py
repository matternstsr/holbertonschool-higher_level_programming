#!/usr/bin/python3
# File: 11-student.py
# Matthew Ernst 6628@holbertonstudents.com
""""""


class Student(object):
    """Student class defined"""

    def __init__(self, first_name, last_name, age):
        """attribs defined for the class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """all in list or all"""
        if attrs is None:
            return self.__dict__
        dict = {}
        for present, value in self.__dict__.items():
            if present in attrs:
                dict[present] = value
        return dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for present, value in json.items():
            setattr(self, present, value)
