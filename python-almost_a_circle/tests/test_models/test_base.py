#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
" I dont know what I need here!!!!!!!!!!!!"

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
