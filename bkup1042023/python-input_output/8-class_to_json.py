#!/usr/bin/python3
# 8-class_to_json.py
# Matthew Ernst 6628@holbertonstudents.com
"""Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:
Prototype: def class_to_json(obj):
obj is an instance of a Class
All attributes of the obj Class are serializable: list, dictionary,
string, integer and boolean
You are not allowed to import any module"""


def class_to_json(obj):
    """Serialize class attributes to dictionary
    obj (object): object to be serialized"""
    return (obj.__dict__)
