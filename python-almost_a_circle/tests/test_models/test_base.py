#!/usr/bin/python3
"""Describes the unittests for base.py file

Unittest classes:
    TestBase_instantiation - line 21
    TestBase_to_json_string - line 100
    TestBase_from_json_string - line 146
    TestBase_create - line 200
    TestBase_save_to_file - line 252
    TestBase_load_from_file - line 330
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Unittests that test instantiation of the new class: Base"""

    def test_no_argument(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)
