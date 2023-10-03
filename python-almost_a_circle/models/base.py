#!/usr/bin/python3
# base.py
# Travis Adamson
""" Declares a new base class """
import json


class Base:
    """Describes a new class: Basee"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new class:

        Args:
            id (int): The id to assign to this obj
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON version of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns an object from the json string provided

        Args:
            json_string (str): A Json string of a list of dictionaries
        Returns:
            Empty list or object represented by the string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class created from dictionary of attribs

        Args:
            **dictionary (dict): Key/value pairs for attibs for init
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def save_to_file(cls, list_objs):
        """Write json rep of a list of objects to a file

        Args:
            list_objs (list): A list of Base inherited objects
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_dictionaries = [ob.to_dictionary() for ob in list_objs]
                json_file.write(Base.to_json_string(list_dictionaries))

    @classmethod
    def load_from_file(cls):
        """Returns a list of classes created from json strings

        Reads from <cls.__name__>.json

        Returns:
            Empty list or a list of created classes
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as json_file:
                list_dictionaries = Base.from_json_string(json_file.read())
                return [cls.create(**d) for d in list_dictionaries]
        except IOError:
            return []