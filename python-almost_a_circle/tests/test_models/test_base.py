#!/usr/bin/python3

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
