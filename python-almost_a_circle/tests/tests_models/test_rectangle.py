#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


class TestRectangleInstantiation(unittest.TestCase):
    def test_no_argument(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_valid_rectangle_instantiation(self):
        rect = Rectangle(5, 10)  # Provide valid width and height
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)

    def test_width_and_height_edge_case(self):
        rect = Rectangle(1, 1)  # Minimum valid dimensions
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 1)

    def test_x_and_y_zero_case(self):
        rect = Rectangle(5, 5, 0, 0)  # Zero for x and y
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-5, 10)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            Rectangle(5, -10)

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -1, 0)

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 0, -1)

    def test_non_integer_width(self):
        with self.assertRaises(TypeError):
            Rectangle(5.5, 10)

    def test_non_integer_height(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 10.5)

    def test_non_integer_x(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 10, 2.5, 0)

    def test_non_integer_y(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 10, 0, 2.5)

    def test_given_id(self):
        rect = Rectangle(5, 10)  # Do not pass 'id' argument
        self.assertNotEqual(rect.id, 25)

    def test_bool_id(self):
        with self.assertRaises(TypeError):
            Rectangle(False, False)

    def test_bytearray_id(self):
        with self.assertRaises(TypeError):
            Rectangle(bytearray(b'abcd1234'))

    def test_bytes_id(self):
        with self.assertRaises(TypeError):
            Rectangle(b'Testing')

    def test_complex_id(self):
        with self.assertRaises(TypeError):
            Rectangle(complex(6))

    def test_dict_id(self):
        with self.assertRaises(TypeError):
            Rectangle({"key": "value"})

    def test_float_id(self):
        with self.assertRaises(TypeError):
            Rectangle(3.3)

    def test_frozenset_id(self):
        with self.assertRaises(TypeError):
            Rectangle(frozenset({4, 5, 6}))

    def test_inf_id(self):
        with self.assertRaises(TypeError):
            Rectangle(float('-inf'))

    def test_memoryview_id(self):
        with self.assertRaises(TypeError):
            Rectangle(memoryview(b'abcd1234'))

    def test_nan_id(self):
        with self.assertRaises(TypeError):
            Rectangle(float('nan'))

    def test_range_id(self):
        with self.assertRaises(TypeError):
            Rectangle(range(4))

    def test_set_id(self):
        with self.assertRaises(TypeError):
            Rectangle({10, 20, 30, 40})

    def test_str_id(self):
        with self.assertRaises(TypeError):
            Rectangle("Test")

    def test_tuple_id(self):
        with self.assertRaises(TypeError):
            Rectangle((1, 2, 3))


class TestRectangleMethods(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_display(self, mock_stdout):
        rect = Rectangle(4, 3)
        rect.display()
        self.assertEqual(mock_stdout.getvalue(), "####\n####\n####\n")

    def test_area_calculation(self):
        rect = Rectangle(7, 3)
        self.assertEqual(rect.area(), 21)

    def test_display_with_offset(self):
        rect = Rectangle(4, 3, 2, 1)
        expected_output = "  ####\n  ####\n  ####\n"
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            rect.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update_with_valid_args(self):
        rect = Rectangle(5, 10)
        rect.update(1, 7, 8, 2, 3)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_update_with_invalid_args(self):
        rect = Rectangle(5, 10)
        with self.assertRaises(ValueError):
            rect.update(1, -7, 8, 2, 3)

    def test_to_dictionary(self):
        rect = Rectangle(5, 10, 2, 3, 1)
        expected_dict = {
            'id': 1,
            'width': 5,
            'height': 10,
            'x': 2,
            'y': 3
        }
        self.assertEqual(rect.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
