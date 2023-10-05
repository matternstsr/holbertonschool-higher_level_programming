#!/usr/bin/python3

import unittest
from models.square import Square
from io import StringIO
from unittest.mock import patch
import os


class TestSquareInstantiation(unittest.TestCase):
    def test_no_argument(self):
        with self.assertRaises(TypeError):
            square1 = Square()

    def test_valid_square_instantiation(self):
        square = Square(5)  # Provide valid size
        self.assertEqual(square.size, 5)

    """def test_invalid_square_instantiation_with_two_arguments(self):
        with self.assertRaises(TypeError):
            square = Square(5, 10)"""

    def test_given_id(self):
        square = Square(5, 1, 2, 25)
        self.assertEqual(square.id, 25)

    def test_bool_id(self):
        with self.assertRaises(TypeError):
            square = Square(False)

    def test_bytearray_id(self):
        with self.assertRaises(TypeError):
            square = Square(bytearray(b'abcd1234'))

    def test_bytes_id(self):
        with self.assertRaises(TypeError):
            square = Square(b'Testing')

    def test_complex_id(self):
        with self.assertRaises(TypeError):
            square = Square(complex(6))

    def test_dict_id(self):
        with self.assertRaises(TypeError):
            square = Square({"key": "value"})

    def test_float_id(self):
        with self.assertRaises(TypeError):
            square = Square(3.3)

    def test_frozenset_id(self):
        with self.assertRaises(TypeError):
            square = Square(frozenset({4, 5, 6}))

    def test_inf_id(self):
        with self.assertRaises(TypeError):
            square = Square(float('-inf'))

    def test_memoryview_id(self):
        with self.assertRaises(TypeError):
            square = Square(memoryview(b'abcd1234'))

    def test_nan_id(self):
        with self.assertRaises(TypeError):
            square = Square(float('nan'))

    def test_range_id(self):
        with self.assertRaises(TypeError):
            square = Square(range(4))

    def test_set_id(self):
        with self.assertRaises(TypeError):
            square = Square({10, 20, 30, 40})

    def test_str_id(self):
        with self.assertRaises(TypeError):
            square = Square("Test")

    def test_tuple_id(self):
        with self.assertRaises(TypeError):
            square = Square((1, 2, 3))
    def test_no_argument(self):
        with self.assertRaises(TypeError):
            square1 = Square()

    def test_valid_square_instantiation(self):
        square = Square(5)  # Provide valid size
        self.assertEqual(square.size, 5)

    def test_given_id(self):
        square = Square(5, 1, 2, 25)
        self.assertEqual(square.id, 25)

    # Add more tests for invalid ID data types

    def test_size_setter_invalid_value(self):
        with self.assertRaises(ValueError):
            square = Square(0)

    def test_size_setter_negative_value(self):
        with self.assertRaises(ValueError):
            square = Square(-5)

    def test_update_method(self):
        square = Square(4)
        square.update(1, 2, 3, 4)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_to_dictionary_method(self):
        square = Square(4, 1, 2, 5)
        dictionary = square.to_dictionary()
        expected = {'id': 5, 'size': 4, 'x': 1, 'y': 2}
        self.assertEqual(dictionary, expected)

    def test_display_method(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            square = Square(4, 2, 1)
            square.display()
            self.assertEqual(mock_stdout.getvalue(), "
    # ... Other test cases ...


class TestSquareMethods(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_display(self, mock_stdout):
        square = Square(4)
        square.display()
        self.assertEqual(mock_stdout.getvalue(), "####\n####\n####\n####\n")

    # ... Other test cases ...
    def test_display(self, mock_stdout):
        square = Square(4)
        square.display()
        self.assertEqual(mock_stdout.getvalue(), "####\n####\n####\n####\n")

    def test_str_method(self):
        square = Square(5, 2, 3, 10)
        self.assertEqual(str(square), "[Square] (10) 2/3 - 5")

    def test_equality(self):
        square1 = Square(4, 2, 3)
        square2 = Square(4, 2, 3)
        self.assertEqual(square1, square2)

    def test_inequality(self):
        square1 = Square(4, 2, 3)
        square2 = Square(5, 2, 3)
        self.assertNotEqual(square1, square2)

if __name__ == "__main__":
    unittest.main()
