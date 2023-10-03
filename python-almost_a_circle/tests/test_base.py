#!/usr/bin/python3
"""
A module that test differents behaviors
of the Base class
"""
import unittest
import pep8
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """A class to test the Base Class"""
    def test_pep8_base(self):
        """Test that checks PEP8"""
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/base.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_id_as_positive(self):
        """positive Base Class id"""
        base_instance = Base(10)
        self.assertEqual(base_instance.id, 10)
        base_instance = Base(5)
        self.assertEqual(base_instance.id, 5)

    def test_id_as_negative(self):
        """negative Base Class id"""
        base_instance = Base(-10)
        self.assertEqual(base_instance.id, -10)
        base_instance = Base(-5)
        self.assertEqual(base_instance.id, -5)

    def test_id_as_none(self):
        """None with Base Class id"""
        base_instance = Base()
        self.assertEqual(base_instance.id, 1)
        base_instance = Base(None)
        self.assertEqual(base_instance.id, 2)

    def test_string_id(self):
        base_instance = Base('Python got really hard')
        self.assertEqual(base_instance.id, 'Python got really hard')
        base_instance = Base('Python is picky')
        self.assertEqual(base_instance.id, 'Python is picky')

    def test_empty_to_json_string(self):
        """to_json_string no data"""
        empty_data = []
        json_data = Base.to_json_string(empty_data)
        self.assertEqual(json_data, "[]")

        empty_data = None
        json_data = Base.to_json_string(empty_data)
        self.assertEqual(json_data, "[]")

    def test_instance(self):
        """Checking instance"""
        base_instance = Base()
        self.assertEqual(type(base_instance), Base)
        self.assertTrue(isinstance(base_instance, Base))

    def test_to_json_string(self):
        """to_json_string from normal strings"""
        rect_data = {'id': 10, 'x': 15, 'y': 5, 'width': 20, 'height': 10}
        json_data = Base.to_json_string([rect_data])

        self.assertTrue(isinstance(rect_data, dict))
        self.assertTrue(isinstance(json_data, str))
        self.assertCountEqual(
            json_data,
            '{["id": 10, "x": 15, "y": 5, "width": 20, "height": 10]}'
        )

    def test_wrong_to_json_string(self):
        """to_json_string method gone wrong"""
        json_data = Base.to_json_string(None)
        self.assertEqual(json_data, "[]")

        warn = ("to_json_string() missing 1 required positional argument: " +
                "'list_dictionaries'")

        with self.assertRaises(TypeError) as msg:
            Base.to_json_string()

        self.assertEqual(warn, str(msg.exception))

        warn = "to_json_string() takes 1 positional argument but 2 were given"

        with self.assertRaises(TypeError) as msg:
            Base.to_json_string([{43, 87}], [{22, 17}])

        self.assertEqual(warn, str(msg.exception))

    def test_wrong_save_to_file(self):
        """Test the save_to_file method"""
        with self.assertRaises(AttributeError) as msg:
            Base.save_to_file([Base(1), Base(2)])

        self.assertEqual(
             "'Base' object has no attribute 'to_dictionary'",
             str(msg.exception)
        )

    def test_load_from_file(self):
        """Test the load_from_file method"""
        if os.path.exists("Base.json"):
            os.remove("Base.json")

        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        if os.path.exists("Square.json"):
            os.remove("Square.json")

        rect_output = Rectangle.load_from_file()
        self.assertEqual(rect_output, [])

        square_output = Square.load_from_file()
        self.assertEqual(square_output, [])

        warn = "load_from_file() takes 1 positional argument but 2 were given"

        with self.assertRaises(TypeError) as msg:
            Rectangle.load_from_file('Monty Python')

        self.assertEqual(warn, str(msg.exception))

        """0,2,22,25,36,38,42,48,52,63,65,83"""
