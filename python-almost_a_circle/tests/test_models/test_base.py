#!/usr/bin/python3
import pep8
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
" I dont know what I need here!!!!!!!!!!!!"


class TestBase_instantiation(unittest.TestCase):
    """ This is a class that tests the base class"""

    def test_id_as_negative(self):
        """
        Test for a negative Base Class id
        """
        base_instance = Base(-100)
        self.assertEqual(base_instance.id, -100)
        base_instance = Base(-10)
        self.assertEqual(base_instance.id, -10)

    def test_id_as_positive(self):
        """
        Test for a positive Base Class id
        """
        base_instance = Base(100)
        self.assertEqual(base_instance.id, 100)
        base_instance = Base(10)
        self.assertEqual(base_instance.id, 10)

    def test_pep8_base(self):
        """
        Test that checks PEP8
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/base.py'])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warnings).")
