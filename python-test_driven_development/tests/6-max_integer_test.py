#!/usr/bin/python3
# 6-max_integer_test.py
# Matthew Ernst  <6628@holbertonstudents.com>
#File is present - good 
#All unittest passed
#Test for “max at the end” exists
#Test for “max at the beginning” exists
#Test for “max in the middle” exists
#Test for “one negative number in the list” exists
#Test for “only negative numbers in the list” exists
#Test for “list of one element” exists
#Test for “list is empty” exists
#you will write unittests for the function def max_integer(list=[]):.
#Your test file should be inside a folder tests
#You have to use the unittest module
#Your test file should be python files (extension: .py)
#should be exec using command: python3 -m unittest tests.6-max_integer_test
#All tests you make must be passable by the function below
"""uni-tests for 6-max_integer"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """testing for max integer"""
    
    def test_empty_list(self):
        """Test when the list is empty"""
        self.assertIsNone(max_integer([]))
        
    def test_empty_string(self):
        """Tests against an empty string"""
        self.assertEqual(max_integer(""), None)
        
    def test_sorted_list(self):
        """Tests against a sorted list"""
        sorted_list = [4, 5, 6, 7]
        self.assertEqual(max_integer(sorted_list), 6)
    
    def test_single_element(self):
        """Test with a list containing a single element"""
        self.assertEqual(max_integer([80]), 80)

    def test_max_dups(self):
        """Test with a list containing duplicate maximum values"""
        self.assertEqual(max_integer([9, 9, 9, 9]), 9)

    def test_negative_integers(self):
        """Test with a list of negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)


        
if __name__ == '__main__':
    unittest.main()