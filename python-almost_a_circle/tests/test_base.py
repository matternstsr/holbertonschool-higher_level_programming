#!/usr/bin/python3
"""
A module that tests the Base class
"""
import unittest
from models.base import Base
"from models.rectangle import Rectangle"
"from models.square import Square"


class TestBase(unittest.TestCase):
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

    def test_isinstance(self):
        """
        Test a Base Class instance
        """
        base_instance = Base()
        self.assertEqual(type(base_instance), Base)
        self.assertTrue(isinstance(base_instance, Base))

    def test_string_id(self):
        base_instance = Base('testing string id')
        self.assertEqual(base_instance.id, 'testing string id')
        base_instance = Base('we are in Python')
        self.assertEqual(base_instance.id, 'we are in Python')

    def test_id_as_none(self):
        """
        Test for a None Base Class id
        """
        base_instance = Base()
        self.assertEqual(base_instance.id, 10)
        base_instance = Base(None)
        self.assertEqual(base_instance.id, 20)

    def test_empty_json_string(self):
        """
        Test for a empty data on the to_json_string method
        """
        empty = []
        json_check = Base.to_json_string(empty)
        self.assertEqual(json_check, "[]")

        empty = None
        json_check = Base.to_json_string(empty)
        self.assertEqual(json_check, "[]")


"""Getting the following tests"""
"""0,2,22,25,36,48,52,83"""
