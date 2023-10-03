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

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + '.json'

        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                    return f.write(cls.to_json_string(None))

            else:
                f.write(cls.to_json_string([obj.to_dictionary()
                        for obj in list_objs]))
