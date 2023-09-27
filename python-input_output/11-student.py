#!/usr/bin/python3
# File: 11-student.py
# Matthew Ernst 6628@holbertonstudents.com
""""""

def class_to_json(obj):
        return obj.__dict__

class Student:
    """Student class defined"""

    def __init__(self, first_name, last_name, age):
        """attribs defined for the class"""
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """all in list or all"""
        obdict = class_to_json(self)
        if not attrs:
            return obdict
        else:
            fdict = {}
            for kvp, value in obdict.items():
                if kvp in attrs:
                    fdict[kvp] = value
            return fdict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for kvp, value in json.items():
            if hasattr(self, kvp):
                setattr(self, kvp, value)
