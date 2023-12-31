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

    @staticmethod
    def from_json_string(json_string):
        """Returns list from the JSON string representation `json_string`."""
        try:
            return json.loads(json_string)
        except (ValueError, TypeError):
            return []

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set:"""
        created = None
        if cls.__name__ == 'Rectangle':
            created = cls(1, 1)
        elif cls.__name__ == 'Square':
            created = cls(1)
        cls.update(created, **dictionary)
        return created
"""18. Dictionary to Instance
Update the class Base by adding the class method def
create(cls, **dictionary): that returns an instance with all attributes
already set:

**dictionary can be thought of as a double pointer to a dictionary
To use the update method to assign all attributes, you must create
a “dummy” instance before:
Create a Rectangle or Square instance with “dummy” mandatory attributes
(width, height, size, etc.)
Call update instance method to this “dummy” instance to apply your
real values
You must use the method def update(self, *args, **kwargs)
**dictionary must be used as **kwargs of the method update
You are not allowed to use eval"""