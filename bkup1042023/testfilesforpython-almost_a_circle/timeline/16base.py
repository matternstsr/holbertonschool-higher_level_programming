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
"""16. JSON string to file
Update the class Base by adding the class method def
save_to_file(cls, list_objs): that writes the JSON string
representation of list_objs to a file:
list_objs is a list of instances who inherits of Base - example:
    list of Rectangle or list of Square instances
If list_objs is None, save an empty list
The filename must be: <Class name>.json - example: Rectangle.json
You must use the static method to_json_string (created before)
You must overwrite the file if it already exists""""