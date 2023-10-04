#!/usr/bin/python3

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):
    def test_str_id(self):
        self.assertEqual("Test", Base("Test").id)

    def test_given_id(self):
        self.assertEqual(25, Base(25).id)

    def test_no_argument(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 2)

    def test_complex_id(self):
        self.assertEqual(complex(6), Base(complex(6)).id)

    def test_dict_id(self):
        self.assertEqual({"key": "value"}, Base({"key": "value"}).id)

    def test_bool_id(self):
        self.assertEqual(False, Base(False).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2, 3), Base((1, 2, 3)).id)

    def test_set_id(self):
        self.assertEqual({10, 20, 30, 40}, Base({10, 20, 30, 40}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({4, 5, 6}), Base(frozenset({4, 5, 6})).id)

    def test_float_id(self):
        self.assertEqual(3.3, Base(3.3).id)

    def test_range_id(self):
        self.assertEqual(range(4), Base(range(4)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Testing', Base(b'Testing').id)

    def test_bytearray_id(self):
        self.assertEqual(
            bytearray(b'abcd1234'), Base(bytearray(b'abcd1234')).id)

    def test_memoryview_id(self):
        self.assertEqual(
            memoryview(b'abcd1234'), Base(memoryview(b'abcd1234')).id)

    def test_inf_id(self):
        self.assertEqual(float('-inf'), Base(float('-inf')).id)

    def test_nan_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_arguments(self):
        with self.assertRaises(TypeError):
            Base(15, 20)


class TestBaseToJsonString(unittest.TestCase):
    def test_to_json_string_rectangle_type(self):
        r1 = Rectangle(10, 5, 1, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([r1.to_dictionary()])))

    def test_to_json_string_rectangle_one_dicttionary(self):
        r1 = Rectangle(10, 5, 1, 3, 4)
        self.assertTrue(len(Base.to_json_string([r1.to_dictionary()])) == 54)

    def test_to_json_string_rectangle_two_dictionaries(self):
        r1 = Rectangle(10, 5, 1, 3, 4)
        r2 = Rectangle(7, 3, 2, 4, 5)
        list_dictionaries = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dictionaries)) == 107)

    def test_to_json_string_square_type(self):
        s1 = Square(15, 3, 1, 2)
        self.assertEqual(str, type(Base.to_json_string([s1.to_dictionary()])))

    def test_to_json_string_square_one_dictionary(self):
        s1 = Square(15, 3, 1, 2)
        self.assertTrue(len(Base.to_json_string([s1.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dictionaries(self):
        s1 = Square(15, 3, 1, 2)
        s2 = Square(12, 4, 3, 5)
        list_dictionaries = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dictionaries)) == 78)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_arguments(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_too_many_arguments(self):
        with self.assertRaises(TypeError):
            Base.to_json_string("[]", 10)


class TestBaseFromJsonString(unittest.TestCase):
    def test_from_json_string_type(self):
        list_in = [{"id": 18, "width": 2, "height": 2}]
        json_list_in = Rectangle.to_json_string(list_in)
        list_out = Rectangle.from_json_string(json_list_in)
        self.assertEqual(list, type(list_out))

    def test_from_json_string_one_rect(self):
        list_in = [{"id": 18, "width": 2, "height": 2, "x": 1}]
        json_list_in = Rectangle.to_json_string(list_in)
        list_out = Rectangle.from_json_string(json_list_in)
        self.assertEqual(list_in, list_out)

    def test_from_json_string_two_rect(self):
        list_in = [
            {"id": 10, "width": 2, "height": 2, "x": 1, "y": 1},
            {"id": 8, "width": 3, "height": 3, "x": 2, "y": 2},
        ]
        json_list_in = Rectangle.to_json_string(list_in)
        list_out = Rectangle.from_json_string(json_list_in)
        self.assertEqual(list_in, list_out)

    def test_from_json_string_one_square(self):
        list_in = [{"id": 10, "size": 2}]
        json_list_in = Square.to_json_string(list_in)
        list_out = Square.from_json_string(json_list_in)
        self.assertEqual(list_in, list_out)

    def test_from_json_string_two_square(self):
        list_in = [
            {"id": 10, "size": 3},
            {"id": 8, "size": 2},
        ]
        json_list_in = Square.to_json_string(list_in)
        list_out = Square.from_json_string(json_list_in)
        self.assertEqual(list_in, list_out)

    def test_from_json_string_none(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_arguments(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_too_many_arguments(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 10)


class TestBaseCreate(unittest.TestCase):
    def test_create_rectangle_orig(self):
        rect1 = Rectangle(10, 9, 8, 5, 2)
        rect1_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dict)
        self.assertEqual("[Rectangle] (3) 8/5 - 10/9", str(rect1))

    def test_create_rectangle_new(self):
        rect1 = Rectangle(5, 4, 2, 3, 1)
        rect1_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dict)
        self.assertEqual("[Rectangle] (1) 2/3 - 5/4", str(rect2))

    def test_create_rectangle_is(self):
        rect1 = Rectangle(5, 4, 2, 3, 1)
        rect1_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dict)
        self.assertIsNot(rect1, rect2)

    def test_create_rectangle_equals(self):
        rect1 = Rectangle(5, 4, 2, 3, 1)
        rect1_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dict)
        self.assertNotEqual(rect1, rect2)

    def test_create_square_orig(self):
        sq1 = Square(4, 5, 6, 7)
        sq1_dict = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dict)
        self.assertEqual("[Square] (7) 5/6 - 4", str(sq1))

    def test_create_square_new(self):
        sq1 = Square(3, 2, 1, 4)
        sq1_dict = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dict)
        self.assertEqual("[Square] (4) 2/1 - 3", str(sq2))

    def test_create_square_is(self):
        sq1 = Square(3, 2, 1, 4)
        sq1_dict = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dict)
        self.assertIsNot(sq1, sq2)

    def test_create_square_equals(self):
        sq1 = Square(3, 2, 1, 4)
        sq1_dict = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dict)
        self.assertNotEqual(sq1, sq2)


class TestBaseSaveToFile(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):
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

    def test_save_to_file_single_rect(self):
        rect1 = Rectangle(7, 3, 2, 4, 5)
        Rectangle.save_to_file([rect1])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 53)

    def test_save_to_file_multi_rect(self):
        rect1 = Rectangle(7, 3, 2, 4, 5)
        rect2 = Rectangle(10, 2, 3, 3, 8)
        Rectangle.save_to_file([rect1, rect2])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 105)

    def test_save_to_file_single_square(self):
        sq1 = Square(5, 2, 2, 1)
        Square.save_to_file([sq1])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 38)

    def test_save_to_file_multi_squares(self):
        sq1 = Square(5, 2, 2, 1)
        sq2 = Square(12, 4, 3, 5)
        Square.save_to_file([sq1, sq2])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 78)

    def test_save_to_file_using_cls_filename(self):
        sq1 = Square(5, 2, 2, 1)
        Base.save_to_file([sq1])
        with open("Base.json", "r") as file:
            self.assertTrue(len(file.read()) == 38)

    def test_save_to_file_overwrite_file(self):
        sq1 = Square(5, 2, 2, 1)
        Square.save_to_file([sq1])
        sq1 = Square(10, 3, 3, 2)
        Square.save_to_file([sq1])
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
    @classmethod
    def tearDownClass(cls):
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

    def test_load_from_file_one_rect(self):
        rect1 = Rectangle(3, 7, 1, 2, 6)
        rect2 = Rectangle(12, 4, 3, 5, 8)
        Rectangle.save_to_file([rect1, rect2])
        list_rect_out = Rectangle.load_from_file()
        self.assertEqual(str(rect1), str(list_rect_out[0]))

    def test_load_from_file_second_rect(self):
        rect1 = Rectangle(3, 7, 1, 2, 6)
        rect2 = Rectangle(12, 4, 3, 5, 8)
        Rectangle.save_to_file([rect1, rect2])
        list_rect_out = Rectangle.load_from_file()
        self.assertEqual(str(rect2), str(list_rect_out[1]))

    def test_load_from_file_rect_type(self):
        rect1 = Rectangle(3, 7, 1, 2, 6)
        rect2 = Rectangle(12, 4, 3, 5, 8)
        Rectangle.save_to_file([rect1, rect2])
        list_rect_out = Rectangle.load_from_file()
        self.assertTrue(all(type(ob) is Rectangle for ob in list_rect_out))

    def test_load_from_file_one_square(self):
        sq1 = Square(4, 5, 6, 7)
        sq2 = Square(11, 2, 3, 1)
        Square.save_to_file([sq1, sq2])
        list_sq_out = Square.load_from_file()
        self.assertEqual(str(sq1), str(list_sq_out[0]))

    def test_load_from_file_second_square(self):
        sq1 = Square(4, 5, 6, 7)
        sq2 = Square(11, 2, 3, 1)
        Square.save_to_file([sq1, sq2])
        list_sq_out = Square.load_from_file()
        self.assertEqual(str(sq2), str(list_sq_out[1]))

    def test_load_from_file_square_type(self):
        sq1 = Square(4, 5, 6, 7)
        sq2 = Square(11, 2, 3, 1)
        Square.save_to_file([sq1, sq2])
        list_sq_out = Square.load_from_file()
        self.assertTrue(all(type(ob) is Square for ob in list_sq_out))

    def test_load_from_file_no_file(self):
        out = Square.load_from_file()
        self.assertEqual([], out)

    def test_load_from_file_too_many_arguments(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 10)
