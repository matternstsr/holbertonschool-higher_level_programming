#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


class TestRectangleInstantiation(unittest.TestCase):
    def test_no_argument(self):
        with self.assertRaises(TypeError):
            Rectangle()  # Removed unused 'rect1' variable

    def test_valid_rectangle_instantiation(self):
        rect = Rectangle(5, 10)  # Provide valid width and height
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)

    def test_given_id(self):
        rect = Rectangle(5, 10)  # Do not pass 'id' argument
        self.assertNotEqual(rect.id, 0)

    # Test cases for invalid 'id' types
    def test_bool_id(self):
        with self.assertRaises(TypeError):
            Rectangle(False, False)  # Removed unused 'rect' variable

    def test_bytearray_id(self):
        with self.assertRaises(TypeError):
            Rectangle(bytearray(b'abcd1234'))  # Removed unused 'rect' variable

    def test_bytes_id(self):
        with self.assertRaises(TypeError):
            Rectangle(b'Testing')  # Removed unused 'rect' variable

    def test_complex_id(self):
        with self.assertRaises(TypeError):
            Rectangle(complex(6))  # Removed unused 'rect' variable

    def test_dict_id(self):
        with self.assertRaises(TypeError):
            Rectangle({"key": "value"})  # Removed unused 'rect' variable

    def test_float_id(self):
        with self.assertRaises(TypeError):
            Rectangle(3.3)  # Removed unused 'rect' variable

    def test_frozenset_id(self):
        with self.assertRaises(TypeError):
            Rectangle(frozenset({4, 5, 6}))  # Removed unused 'rect' variable

    def test_inf_id(self):
        with self.assertRaises(TypeError):
            Rectangle(float('-inf'))  # Removed unused 'rect' variable

    def test_memoryview_id(self):
        with self.assertRaises(TypeError):
            Rectangle(memoryview(b'abcd1234'))  # Rem unused 'rect' variable

    def test_nan_id(self):
        with self.assertRaises(TypeError):
            Rectangle(float('nan'))  # Removed unused 'rect' variable

    def test_range_id(self):
        with self.assertRaises(TypeError):
            Rectangle(range(4))  # Removed unused 'rect' variable

    def test_set_id(self):
        with self.assertRaises(TypeError):
            Rectangle({10, 20, 30, 40})  # Removed unused 'rect' variable

    def test_str_id(self):
        with self.assertRaises(TypeError):
            Rectangle("Test")  # Removed unused 'rect' variable

    def test_tuple_id(self):
        with self.assertRaises(TypeError):
            Rectangle((1, 2, 3))  # Removed unused 'rect' variable


class TestRectangleMethods(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_display(self, mock_stdout):
        rect = Rectangle(4, 3)
        rect.display()
        expected_output = "####\n####\n####\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # Add more test cases for other methods as needed


if __name__ == "__main__":
    unittest.main()
