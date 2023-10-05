#!/usr/bin/python3

import unittest
from models.square import Square
from io import StringIO
from unittest.mock import patch


class TestSquareInstantiation(unittest.TestCase):
    def test_no_argument(self):
        with self.assertRaises(TypeError):
            Square()

    def test_valid_square_instantiation(self):
        square = Square(5)  # Valid size
        self.assertEqual(square.size, 5)

    def test_given_id(self):
        square = Square(5, 1, 2, 25)
        self.assertEqual(square.id, 25)

    # Add more tests for invalid ID data types

    def test_size_setter_invalid_value(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_size_setter_negative_value(self):
        with self.assertRaises(ValueError):
            Square(-5)

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
            self.assertEqual(mock_stdout.getvalue(),
                             "    ####\n    ####\n    ####\n    ####\n")


class TestSquareMethods(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_display_custom(self, mock_stdout):
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
