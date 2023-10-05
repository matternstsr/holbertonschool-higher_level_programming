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
        square = Square(5)  # Provide valid size
        self.assertEqual(square.size, 5)

    def test_given_id(self):
        square = Square(5, 1, 2, 25)
        self.assertEqual(square.id, 25)

    def test_bool_id(self):
        with self.assertRaises(TypeError):
            Square(False)

    def test_bytearray_id(self):
        with self.assertRaises(TypeError):
            Square(bytearray(b'abcd1234'))

    def test_bytes_id(self):
        with self.assertRaises(TypeError):
            Square(b'Testing')

    def test_complex_id(self):
        with self.assertRaises(TypeError):
            Square(complex(6))

    def test_dict_id(self):
        with self.assertRaises(TypeError):
            Square({"key": "value"})

    def test_float_id(self):
        with self.assertRaises(TypeError):
            Square(3.3)

    def test_frozenset_id(self):
        with self.assertRaises(TypeError):
            Square(frozenset({4, 5, 6}))

    def test_inf_id(self):
        with self.assertRaises(TypeError):
            Square(float('-inf'))

    def test_memoryview_id(self):
        with self.assertRaises(TypeError):
            Square(memoryview(b'abcd1234'))

    def test_nan_id(self):
        with self.assertRaises(TypeError):
            Square(float('nan'))

    def test_range_id(self):
        with self.assertRaises(TypeError):
            Square(range(4))

    def test_set_id(self):
        with self.assertRaises(TypeError):
            Square({10, 20, 30, 40})

    def test_str_id(self):
        with self.assertRaises(TypeError):
            Square("Test")

    def test_tuple_id(self):
        with self.assertRaises(TypeError):
            Square((1, 2, 3))


class TestSquareMethods(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_display(self, mock_stdout):
        square = Square(4)
        square.display()
        self.assertEqual(mock_stdout.getvalue(), "####\n####\n####\n####\n")

    def test_str_representation(self):
        square = Square(5, 2, 3, 7)
        self.assertEqual(str(square), "[Square] (7) 2/3 - 5")

    def test_update_method_args(self):
        square = Square(3, 1, 1, 10)
        square.update(1, 5, 5, 2)
        self.assertEqual(str(square), "[Square] (1) 5/5 - 2")

    def test_update_method_kwargs(self):
        square = Square(3, 1, 1, 10)
        square.update(id=2, x=2, size=4, y=3)
        self.assertEqual(str(square), "[Square] (2) 2/3 - 4")

    def test_to_dictionary_method(self):
        square = Square(4, 2, 3, 7)
        square_dict = square.to_dictionary()
        expected_dict = {'id': 7, 'size': 4, 'x': 2, 'y': 3}
        self.assertEqual(square_dict, expected_dict)

    def test_size_property(self):
        square = Square(4)
        square.size = 6
        self.assertEqual(square.size, 6)
        self.assertEqual(square.width, 6)
        self.assertEqual(square.height, 6)

    def test_invalid_size_setter(self):
        square = Square(4)
        with self.assertRaises(ValueError):
            square.size = -2

    def test_invalid_size_type_setter(self):
        square = Square(4)
        with self.assertRaises(TypeError):
            square.size = "invalid"

    def test_invalid_x_type_setter(self):
        square = Square(4)
        with self.assertRaises(TypeError):
            square.x = "invalid"

    def test_invalid_y_type_setter(self):
        square = Square(4)
        with self.assertRaises(TypeError):
            square.y = "invalid"

    def test_invalid_x_negative_setter(self):
        square = Square(4)
        with self.assertRaises(ValueError):
            square.x = -2

    def test_invalid_y_negative_setter(self):
        square = Square(4)
        with self.assertRaises(ValueError):
            square.y = -2

    def test_area_method(self):
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_invalid_area_method(self):
        square = Square(-2)
        with self.assertRaises(ValueError):
            square.area()

    def test_invalid_area_type_method(self):
        square = Square("invalid")
        with self.assertRaises(TypeError):
            square.area()

    def test_invalid_id_type(self):
        with self.assertRaises(TypeError):
            Square(5, 2, 3, "invalid_id")

    def test_invalid_x_type(self):
        with self.assertRaises(TypeError):
            Square(5, "invalid_x", 3, 7)

    def test_invalid_y_type(self):
        with self.assertRaises(TypeError):
            Square(5, 2, "invalid_y", 7)

    def test_negative_size(self):
        with self.assertRaises(ValueError):
            Square(-5)

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            Square(5, -2, 3, 7)

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            Square(5, 2, 3, -7)

    def test_eq_method_true(self):
        square1 = Square(5)
        square2 = Square(5)
        self.assertTrue(square1 == square2)

    def test_eq_method_false(self):
        square1 = Square(5)
        square2 = Square(6)
        self.assertFalse(square1 == square2)


if __name__ == "__main__":
    unittest.main()
