#!/usr/bin/python3

import os
import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquareInstantiation(unittest.TestCase):
    def test_no_argument(self):
        square1 = Square()
        square2 = Square()
        self.assertEqual(square1.id, square2.id - 2)

    def test_given_id(self):
        self.assertEqual(25, Square(25).id)

    def test_str_id(self):
        self.assertEqual("Test", Square("Test").id)

    def test_float_id(self):
        self.assertEqual(3.3, Square(3.3).id)

    def test_complex_id(self):
        self.assertEqual(complex(6), Square(complex(6)).id)

    def test_dict_id(self):
        self.assertEqual({"key": "value"}, Square({"key": "value"}).id)

    def test_bool_id(self):
        self.assertEqual(False, Square(False).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2, 3), Square((1, 2, 3)).id)

    def test_set_id(self):
        self.assertEqual({10, 20, 30, 40}, Square({10, 20, 30, 40}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({4, 5, 6}), Square(frozenset({4, 5, 6})).id)

    def test_range_id(self):
        self.assertEqual(range(4), Square(range(4)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Testing', Square(b'Testing').id)

    def test_bytearray_id(self):
        self.assertEqual(
            bytearray(b'abcd1234'), Square(bytearray(b'abcd1234')).id)

    def test_memoryview_id(self):
        self.assertEqual(
            memoryview(b'abcd1234'), Square(memoryview(b'abcd1234')).id)

    def test_inf_id(self):
        self.assertEqual(float('-inf'), Square(float('-inf')).id)

    def test_nan_id(self):
        self.assertNotEqual(float('nan'), Square(float('nan')).id)

    def test_two_arguments(self):
        with self.assertRaises(TypeError):
            square = Square(15, 20)

class TestSquareMethods(unittest.TestCase):
    def test_area(self):
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_display(self):
        square = Square(2)
        expected_output = "##\n##\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            square.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        square = Square(3, 2, 1, 7)
        self.assertEqual(str(square), "[Square] (7) 2/1 - 3")

    def test_update_args(self):
        square = Square(2, 4, 5)
        square.update(10, 2, 5, 0)
        self.assertEqual(str(square), "[Square] (10) 5/0 - 2")

    def test_update_kwargs(self):
        square = Square(5, 0, 0, 1)
        square.update(id=10, size=2, x=4, y=5)
        self.assertEqual(str(square), "[Square] (10) 4/5 - 2")

    def test_update_args_and_kwargs(self):
        square = Square(5, 0, 0, 1)
        square.update(10, size=2, x=4, y=5)
        self.assertEqual(str(square), "[Square] (10) 4/5 - 2")

    def test_to_dictionary(self):
        square = Square(5, 2, 3, 1)
        expected_dict = {
            'id': 1,
            'size': 5,
            'x': 2,
            'y': 3
        }
        self.assertEqual(square.to_dictionary(), expected_dict)
