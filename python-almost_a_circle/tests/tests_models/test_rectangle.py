#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch
import os


class TestRectangleInstantiation(unittest.TestCase):
    def test_no_argument(self):
        with self.assertRaises(TypeError):
            rect1 = Rectangle()

    def test_valid_rectangle_instantiation(self):
        rect = Rectangle(5, 10)  # Provide valid width and height
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)

    """def test_invalid_rectangle_instantiation_with_two_arguments(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10)"""

    def test_given_id(self):
        rect = Rectangle(5, 10)  # Do not pass 'id' argument
        self.assertNotEqual(rect.id, 25)

    def test_bool_id(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(False, False)

    def test_bytearray_id(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(bytearray(b'abcd1234'))

    def test_bytes_id(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(b'Testing')

    def test_complex_id(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(complex(6))

    def test_dict_id(self):
        with self.assertRaises(TypeError):
            rect = Rectangle({"key": "value"})

    def test_float_id(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(3.3)

    def test_frozenset_id(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(frozenset({4, 5, 6}))

    def test_inf_id(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(float('-inf'))

    def test_memoryview_id(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(memoryview(b'abcd1234'))

    def test_nan_id(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(float('nan'))

    def test_range_id(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(range(4))

    def test_set_id(self):
        with self.assertRaises(TypeError):
            rect = Rectangle({10, 20, 30, 40})

    def test_str_id(self):
        with self.assertRaises(TypeError):
            rect = Rectangle("Test")

    def test_tuple_id(self):
        with self.assertRaises(TypeError):
            rect = Rectangle((1, 2, 3))

    # ... Other test cases ...


class TestRectangleMethods(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_display(self, mock_stdout):
        rect = Rectangle(4, 3)
        rect.display()
        self.assertEqual(mock_stdout.getvalue(), "####\n####\n####\n")

    # ... Other test cases ...


if __name__ == "__main__":
    unittest.main()
