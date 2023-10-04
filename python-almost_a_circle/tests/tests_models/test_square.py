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

    # ... Other test cases ...


class TestSquareMethods(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_display(self, mock_stdout):
        square = Square(4)
        square.display()
        self.assertEqual(mock_stdout.getvalue(), "####\n####\n####\n####\n")

    # ... Other test cases ...


if __name__ == "__main__":
    unittest.main()
