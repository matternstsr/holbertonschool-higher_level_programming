#!/usr/bin/python3
# base.py
# Matthew Ernst 6628@holbertonstudents.com
"""Makes a Base Class"""
import json


class Base:
    """New Class Base"""
    __nb_objects = 0
    FILE_EXTENSION = '.json'
    ENCODING = 'utf-8'

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

    @classmethod
    def load_from_file(cls):
        """This defines a class method named load_from_file. It's used to
        load instances of the class from a JSON file and return them as a
        list.."""
        file_name = cls.__name__ + cls.FILE_EXTENSION
        """This line constructs the name of the JSON file by combining
        the class name (cls.__name__) with the FILE_EXTENSION constant,
        creating a filename like 'YourClassName.json.'"""
        instances = []
        """This initializes an empty list called instances to
        store the instances loaded from the JSON file."""
        if path.isfile(file_name):
            """This checks if the JSON file with the constructed file_name
            exists in the current directory."""
            with open(file_name, 'r', encoding=cls.ENCODING) as f:
                """If the file exists, this line opens it in read mode ('r')
                with the specified encoding (cls.ENCODING).
                The file is opened within a context manager,
                ensuring it's properly closed after use."""
                dictionary = cls.from_json_string(f.read())
                """This reads the contents of the JSON file (f.read())
                and passes it to the from_json_string class method
                to parse it into a dictionary.
                The resulting dictionary represents the data
                from the JSON file."""
                for obj in dictionary:
                    """This initiates a loop to iterate over each dictionary
                    item in the dictionary. Each item represents data for an
                    instance."""
                    instances.append(cls.create(**obj))

                    """Within the loop, this line creates an
                    instance using the create class method,
                    passing the unpacked obj
                    (keyword arguments) to it.
                    The created instance is then appended
                    to the instances list."""
        return instances
