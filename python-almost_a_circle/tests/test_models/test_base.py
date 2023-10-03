#!/usr/bin/python3

def test_id_as_negative(self):
    """
    Test for a negative Base Class id
    """
    base_instance = Base(-91)
    self.assertEqual(base_instance.id, -91)
    base_instance = Base(-4)
    self.assertEqual(base_instance.id, -4)