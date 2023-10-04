#!/usr/bin/python3

import os
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleInstantiation(unittest.TestCase):
    def test_no_argument(self):
        rect1 = Rectangle()
        rect2 = Rectangle()
        self.assertEqual(rect1.id, rect2.id - 2)

    def test_given_id(self):
        self.assertEqual(25, Rectangle(25).id)

    def test_str_id(self):
        self.assertEqual("Test", Rectangle("Test").id)

    def test_float_id(self):
        self.assertEqual(3.3, Rectangle(3.3).id)

    def test_complex_id(self):
        self.assertEqual(complex(6), Rectangle(complex(6)).id)

    def test_dict_id(self):
        self.assertEqual({"key": "value"}, Rectangle({"key": "value"}).id)

    def test_bool_id(self):
        self.assertEqual(False, Rectangle(False).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2, 3), Rectangle((1, 2, 3)).id)

    def test_set_id(self):
        self.assertEqual({10, 20, 30, 40}, Rectangle({10, 20, 30, 40}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({4, 5, 6}), Rectangle(frozenset({4, 5, 6})).id)

    def test_range_id(self):
        self.assertEqual(range(4), Rectangle(range(4)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Testing', Rectangle(b'Testing').id)

    def test_bytearray_id(self):
        self.assertEqual(
            bytearray(b'abcd1234'), Rectangle(bytearray(b'abcd1234')).id)

    def test_memoryview_id(self):
        self.assertEqual(
            memoryview(b'abcd1234'), Rectangle(memoryview(b'abcd1234')).id)

    def test_inf_id(self):
        self.assertEqual(float('-inf'), Rectangle(float('-inf')).id)

    def test_nan_id(self):
        self.assertNotEqual(float('nan'), Rectangle(float('nan')).id)

    def test_two_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle(15, 20)


class TestRectangleMethods(unittest.TestCase):
    def test_area(self):
        rect = Rectangle(5, 4)
        self.assertEqual(rect.area(), 20)

    def test_display(self):
        rect = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rect.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        rect = Rectangle(3, 4, 2, 1, 7)
        self.assertEqual(str(rect), "[Rectangle] (7) 2/1 - 3/4")

    def test_update_args(self):
        rect = Rectangle(5, 5, 0, 0, 1)
        rect.update(10, 2, 3, 4, 5)
        self.assertEqual(str(rect), "[Rectangle] (10) 4/5 - 2/3")

    def test_update_kwargs(self):
        rect = Rectangle(5, 5, 0, 0, 1)
        rect.update(id=10, width=2, height=3, x=4, y=5)
        self.assertEqual(str(rect), "[Rectangle] (10) 4/5 - 2/3")

    def test_update_args_and_kwargs(self):
        rect = Rectangle(5, 5, 0, 0, 1)
        rect.update(10, width=2, height=3, x=4, y=5)
        self.assertEqual(str(rect), "[Rectangle] (10) 4/5 - 2/3")

    def test_to_dictionary(self):
        rect = Rectangle(5, 5, 0, 0, 1)
        expected_dict = {
            'id': 1,
            'width': 5,
            'height': 5,
            'x': 0,
            'y': 0
        }
        self.assertEqual(rect.to_dictionary(), expected_dict)

