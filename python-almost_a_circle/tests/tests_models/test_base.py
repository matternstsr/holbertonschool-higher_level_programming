#!/usr/bin/python3
"""Base class unittests"""
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):

    def test_class_membership(self):
        """Base class unittest"""
        b0 = Base()
        # Check if b0 is an instance of Base
        self.assertIsInstance(b0, Base)
        # Ensure b0 is not an instance of Rectangle or Square
        self.assertFalse(isinstance(b0, Rectangle))
        self.assertFalse(isinstance(b0, Square))

    def test_no_id_arg(self):
        """Base class ids unittest"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        # Check that IDs are unique integers
        self.assertIsInstance(b1.id, int)
        self.assertIsInstance(b2.id, int)
        self.assertIsInstance(b3.id, int)
        self.assertNotEqual(b1.id, b2.id)
        self.assertNotEqual(b2.id, b3.id)
        self.assertNotEqual(b1.id, b3.id)

    def test_no_id_plus_id_combo(self):
        """Base class ids unittest"""
        b4 = Base(5)
        b5 = Base()
        # Check that IDs are integers and equal to expected values
        self.assertIsInstance(b4.id, int)
        self.assertIsInstance(b5.id, int)
        self.assertEqual(b4.id, 5)
        self.assertEqual(b5.id, 6)  # ID should increment

    def test_to_json_string(self):
        """to_json_string method unittest"""
        r = Rectangle(10, 7, 2, 8)
        rd = r.to_dictionary()
        self.assertIsInstance(rd, dict)
        json_rd = Base.to_json_string([rd])
        self.assertIsInstance(json_rd, str)

        s = Square(10)
        sd = s.to_dictionary()
        self.assertIsInstance(sd, dict)
        json_sd = Base.to_json_string([sd])
        self.assertIsInstance(json_sd, str)

    def test_save_to_file(self):
        """save_to_file method unittest"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        dict_list = []
        with open('Rectangle.json', 'r', encoding='utf-8') as f:
            dict_list = json.load(f)
        self.assertIsInstance(dict_list, list)
        self.assertEqual(len(dict_list), 2)
        list_ref = [
            {'id': 1, 'height': 7, 'x': 2, 'width': 10, 'y': 8},
            {'id': 2, 'height': 4, 'x': 0, 'width': 2, 'y': 0}
        ]
        self.assertListEqual(dict_list, list_ref)

        Square.save_to_file([])
        dict_list = []
        with open('Square.json', 'r', encoding='utf-8') as f:
            dict_list = json.load(f)
        self.assertIsInstance(dict_list, list)
        self.assertEqual(len(dict_list), 0)

        s1 = Square(2, x=1, y=2, id=98)
        s2 = Square(3, x=5, y=7, id=99)
        Square.save_to_file([s1, s2])
        dict_list = []
        with open('Square.json', 'r', encoding='utf-8') as f:
            dict_list = json.load(f)
        self.assertIsInstance(dict_list, list)
        self.assertEqual(len(dict_list), 2)
        list_ref = [
            {'x': 1, 'id': 98, 'size': 2, 'y': 2},
            {'x': 5, 'id': 99, 'size': 3, 'y': 7}
        ]
        self.assertListEqual(dict_list, list_ref)

    def test_from_json_string(self):
        """from_json_string method unittest"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertListEqual(list_output, list_input)

        list_input = []
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertListEqual(list_output, list_input)

    def test_create_method(self):
        """create method unittest"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)
        self.assertNotEqual(r2, r1)

        s1 = Square(5, id=6, x=1, y=2)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertFalse(s1 is s2)
        self.assertNotEqual(s2, s1)

    def test_load_from_file_method(self):
        """load_from_file method unittest"""
        r1 = Rectangle(10, 7, 2, 8, id=10)
        r2 = Rectangle(2, 4, id=11)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        # Add assertions to check that the loaded objects match the expected ones
        self.assertEqual(len(list_rectangles_output), 2)
        self.assertIsInstance(list_rectangles_output[0], Rectangle)
        self.assertIsInstance(list_rectangles_output[1], Rectangle)
        self.assertEqual(list_rectangles_output[0].id, 10)
        self.assertEqual(list_rectangles_output[1].id, 11)

if __name__ == '__main__':
    unittest.main()
