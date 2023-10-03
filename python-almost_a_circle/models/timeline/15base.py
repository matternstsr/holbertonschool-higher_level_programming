#!/usr/bin/python3
# base.py
# Matthew Ernst 6628@holbertonstudents.com
"""Makes a Base Class"""
import json


class Base:
    """New Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes Base Class with id to assign to this obj"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

"""15. Dictionary to JSON string
JSON is one of the standard formats for sharing data representation.
Update the class Base by adding the static method def 
to_json_string(list_dictionaries): that returns the JSON string 
representation of list_dictionaries:
list_dictionaries is a list of dictionaries
If list_dictionaries is None or empty, return the string: "[]"
Otherwise, return the JSON string representation of list_dictionaries"""