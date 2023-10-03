#!/usr/bin/python3
"""
A module that tests the Base class
"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ This is a class that tests the base class"""
    def test_pep8_base(self):
        """
        Test that checks PEP8
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/base.py'])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warnings).")

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

    def test_isinstance(self):
        """
        Test a Base Class instance
        """
        base_instance = Base()
        self.assertEqual(type(base_instance), Base)
        self.assertTrue(isinstance(base_instance, Base))

    def test_string_id(self):
        base_instance = Base('Monty Python')
        self.assertEqual(base_instance.id, 'Monty Python')
        base_instance = Base('Python is cool')
        self.assertEqual(base_instance.id, 'Python is cool')
