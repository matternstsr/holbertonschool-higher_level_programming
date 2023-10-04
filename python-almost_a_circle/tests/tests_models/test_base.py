#!/usr/bin/python3

"""This module contains unit tests for the base.py file.

List of unit test classes:
- TestBaseInstantiation (Line 21)
- TestBaseToJsonString (Line 100)
- TestBaseFromJsonString (Line 146)
- TestBaseCreate (Line 200)
- TestBaseSaveToFile (Line 252)
- TestBaseLoadFromFile (Line 330)
"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseInstantiation(unittest.TestCase):
    """Unit tests for verifying the instantiation of the 'Base' class."""

    def test_no_argument(self):
        instance_a = Base()
        instance_b = Base()
        self.assertEqual(instance_a.id, instance_b.id - 1)

    def test_multiple_instantiations(self):
        instance_a = Base()
        instance_b = Base()
        instance_c = Base()
        self.assertEqual(instance_a.id, instance_c.id - 2)

    def test_given_id(self):
        self.assertEqual(123, Base(123).id)

    def test_id_increment_after_given_id(self):
        instance_a = Base()
        instance_b = Base(123)
        instance_c = Base()
        self.assertEqual(instance_a.id, instance_c.id - 1)

    def test_id_is_public(self):
        instance = Base(123)
        instance.id = 456
        self.assertEqual(456, instance.id)

    def test_nb_is_private(self):
        with self.assertRaises(AttributeError):
            print(Base(456).__nb_instances)

    def test_string_id(self):
        self.assertEqual("Help123", Base("Help123").id)

    def test_float_id(self):
        self.assertEqual(45.6, Base(45.6).id)

    def test_complex_id(self):
        self.assertEqual(complex(7), Base(complex(7)).id)

    def test_dict_id(self):
        self.assertEqual({"k": 10, "v": 20}, Base({"k": 10, "v": 20}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_tuple_id(self):
        self.assertEqual((10, 20), Base((10, 20)).id)

    def test_set_id(self):
        self.assertEqual({10, 20, 30}, Base({10, 20, 30}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        self.assertEqual(range(3), Base(range(3)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python123', Base(b'Python123').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcd123'), Base(bytearray(b'abcd123')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcd123'), Base(memoryview(b'abcd123')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_nan_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_arguments(self):
        with self.assertRaises(TypeError):
            Base(123, 456)

class TestBaseToJsonString(unittest.TestCase):
    """Unit tests for the 'to_json_string' method."""

    def test_rectangle_type(self):
        rectangle = Rectangle(123, 45, 6, 78, 9)
        self.assertEqual(str, type(Base.to_json_string([rectangle.to_dictionary()])))

    def test_rectangle_single_dictionary(self):
        rectangle = Rectangle(123, 45, 6, 78, 9)
        self.assertTrue(len(Base.to_json_string([rectangle.to_dictionary()])) == 99)

    def test_rectangle_multiple_dictionaries(self):
        rectangle1 = Rectangle(123, 45, 6, 78, 9)
        rectangle2 = Rectangle(456, 78, 9, 12, 34)
        list_of_dicts = [rectangle1.to_dictionary(), rectangle2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_of_dicts)) == 198)

    def test_square_type(self):
        square = Square(123, 45, 6, 7)
        self.assertEqual(str, type(Base.to_json_string([square.to_dictionary()])))

    def test_square_single_dictionary(self):
        square = Square(123, 45, 6, 7)
        self.assertTrue(len(Base.to_json_string([square.to_dictionary()])) == 75)

    def test_square_multiple_dictionaries(self):
        square1 = Square(123, 45, 6, 7)
        square2 = Square(456, 78, 9, 10)
        list_of_dicts = [square1.to_dictionary(), square2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_of_dicts)) == 150)

    def test_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_no_arguments(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_too_many_arguments(self):
        with self.assertRaises(TypeError):
            Base.to_json_string("[]", 10)

class TestBaseFromJsonString(unittest.TestCase):
    """Unit tests for the 'from_json_string' method."""

    def test_rectangle_type(self):
        input_list = [{"id": 1, "width": 2, "height": 3}]
        json_input = Rectangle.to_json_string(input_list)
        output_list = Rectangle.from_json_string(json_input)
        self.assertEqual(list, type(output_list))

    def test_single_rectangle(self):
        input_list = [{"id": 1, "width": 2, "height": 3, "x": 4}]
        json_input = Rectangle.to_json_string(input_list)
        output_list = Rectangle.from_json_string(json_input)
        self.assertEqual(input_list, output_list)

    def test_multiple_rectangles(self):
        input_list = [
            {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
            {"id": 2, "width": 5, "height": 4, "x": 3, "y": 2},
        ]
        json_input = Rectangle.to_json_string(input_list)
        output_list = Rectangle.from_json_string(json_input)
        self.assertEqual(input_list, output_list)

    def test_single_square(self):
        input_list = [{"id": 1, "size": 2}]
        json_input = Square.to_json_string(input_list)
        output_list = Square.from_json_string(json_input)
        self.assertEqual(input_list, output_list)

    def test_multiple_squares(self):
        input_list = [
            {"id": 1, "size": 2},
            {"id": 2, "size": 3},
        ]
        json_input = Square.to_json_string(input_list)
        output_list = Square.from_json_string(json_input)
        self.assertEqual(input_list, output_list)

    def test_none(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_empty(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_no_arguments(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_too_many_arguments(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 10)

class TestBaseCreate(unittest.TestCase):
    """Unit tests for the 'create' method."""

    def test_create_rectangle_original(self):
        rectangle1 = Rectangle(10, 9, 8, 5, 2)
        rectangle1_dict = rectangle1.to_dictionary()
        rectangle2 = Rectangle.create(**rectangle1_dict)
        self.assertEqual("[Rectangle] (2) 8/5 - 10/9", str(rectangle1))

    def test_create_rectangle_new(self):
        rectangle1 = Rectangle(10, 9, 8, 5, 2)
        rectangle1_dict = rectangle1.to_dictionary()
        rectangle2 = Rectangle.create(**rectangle1_dict)
        self.assertEqual("[Rectangle] (2) 8/5 - 10/9", str(rectangle2))

    def test_create_rectangle_is_not_same_instance(self):
        rectangle1 = Rectangle(10, 9, 8, 5, 2)
        rectangle1_dict = rectangle1.to_dictionary()
        rectangle2 = Rectangle.create(**rectangle1_dict)
        self.assertIsNot(rectangle1, rectangle2)

    def test_create_rectangle_not_equal(self):
        rectangle1 = Rectangle(10, 9, 8, 5, 2)
        rectangle1_dict = rectangle1.to_dictionary()
        rectangle2 = Rectangle.create(**rectangle1_dict)
        self.assertNotEqual(rectangle1, rectangle2)

    def test_create_square_original(self):
        square1 = Square(2, 3, 1, 4)
        square1_dict = square1.to_dictionary()
        square2 = Square.create(**square1_dict)
        self.assertEqual("[Square] (4) 3/1 - 2", str(square1))

    def test_create_square_new(self):
        square1 = Square(2, 3, 1, 4)
        square1_dict = square1.to_dictionary()
        square2 = Square.create(**square1_dict)
        self.assertEqual("[Square] (4) 3/1 - 2", str(square2))

    def test_create_square_is_not_same_instance(self):
        square1 = Square(2, 3, 1, 4)
        square1_dict = square1.to_dictionary()
        square2 = Square.create(**square1_dict)
        self.assertIsNot(square1, square2)

    def test_create_square_not_equal(self):
        square1 = Square(2, 3, 1, 4)
        square1_dict = square1.to_dictionary()
        square2 = Square.create(**square1_dict)
        self.assertNotEqual(square1, square2)

class TestBaseSaveToFile(unittest.TestCase):
    """Unit tests for the 'save_to_file' method."""

    @classmethod
    def tearDown(self):
        """Delete any previously created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_single_rectangle(self):
        rectangle1 = Rectangle(5, 2, 1, 3, 4)
        Rectangle.save_to_file([rectangle1])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 52)

    def test_save_to_file_multiple_rectangles(self):
        rectangle1 = Rectangle(5, 2, 1, 3, 4)
        rectangle2 = Rectangle(10, 3, 2, 4, 5)
        Rectangle.save_to_file([rectangle1, rectangle2])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 105)

    def test_save_to_file_single_square(self):
        square1 = Square(5, 2, 2, 1)
        Square.save_to_file([square1])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 38)

    def test_save_to_file_multiple_squares(self):
        square1 = Square(5, 2, 2, 1)
        square2 = Square(4, 3, 3, 2)
        Square.save_to_file([square1, square2])
        with open("Square.json", "r") as file:
            file_length = len(file.read())
        self.assertTrue(file_length == 76)

    def test_save_to_file_using_cls_filename(self):
        square1 = Square(5, 2, 2, 1)
        Base.save_to_file([square1])
        with open("Base.json", "r") as file:
            file_length = len(file.read())
        self.assertTrue(file_length == 38)

    def test_save_to_file_overwrite_file(self):
        square1 = Square(5, 2, 2, 1)
        Square.save_to_file([square1])
        square1 = Square(10, 3, 3, 2)
        Square.save_to_file([square1])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_to_file_no_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_too_many_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], 10)

class TestBaseLoadFromFile(unittest.TestCase):
    """Unit tests for the 'load_from_file' method."""

    @classmethod
    def tearDown(self):
        """Delete previously created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_load_from_file_single_rectangle(self):
        rectangle1 = Rectangle(5, 4, 2, 2, 1)
        rectangle2 = Rectangle(10, 2, 3, 3, 2)
        Rectangle.save_to_file([rectangle1, rectangle2])
        loaded_list = Rectangle.load_from_file()
        self.assertEqual(str(rectangle1), str(loaded_list[0]))

    def test_load_from_file_second_rectangle(self):
        rectangle1 = Rectangle(5, 4, 2, 2, 1)
        rectangle2 = Rectangle(10, 2, 3, 3, 2)
        Rectangle.save_to_file([rectangle1, rectangle2])
        loaded_list = Rectangle.load_from_file()
        self.assertEqual(str(rectangle2), str(loaded_list[1]))

    def test_load_from_file_rectangle_type(self):
        rectangle1 = Rectangle(5, 4, 2, 2, 1)
        rectangle2 = Rectangle(10, 2, 3, 3, 2)
        Rectangle.save_to_file([rectangle1, rectangle2])
        loaded_list = Rectangle.load_from_file()
        self.assertTrue(all(isinstance(ob, Rectangle) for ob in loaded_list))

    def test_load_from_file_single_square(self):
        square1 = Square(5, 2, 2, 1)
        square2 = Square(10, 2, 3, 2)
        Square.save_to_file([square1, square2])
        loaded_list = Square.load_from_file()
        self.assertEqual(str(square1), str(loaded_list[0]))

    def test_load_from_file_second_square(self):
        square1 = Square(5, 2, 2, 1)
        square2 = Square(10, 2, 3, 2)
        Square.save_to_file([square1, square2])
        loaded_list = Square.load_from_file()
        self.assertEqual(str(square2), str(loaded_list[1]))

    def test_load_from_file_square_type(self):
        square1 = Square(5, 2, 2, 1)
        square2 = Square(10, 2, 3, 2)
        Square.save_to_file([square1, square2])
        loaded_list = Square.load_from_file()
        self.assertTrue(all(isinstance(ob, Square) for ob in loaded_list))

    def test_load_from_file_no_file(self):
        loaded_list = Square.load_from_file()
        self.assertEqual([], loaded_list)

    def test_load_from_file_too_many_arguments(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 10)
