#!/usr/bin/python3
# 8-class_to_json.py
# Matthew Ernst 6628@holbertonstudents.com
"""Write a class Student that defines a student by:
Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age:
def __init__(self, first_name, last_name, age):
Public method def to_json(self): that retrieves a dictionary
representation of a Student instance (same as 8-class_to_json.py)
You are not allowed to import any module"""


def to_json(self):
    """Serialize class attributes to dictionary
    obj (object): object to be serialized"""
    def __init__(self, first_name, last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
           
    
    return (obj.__dict__)
