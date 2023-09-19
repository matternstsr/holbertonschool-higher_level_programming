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

"""======================================================================
ERROR: tests (unittest.loader._FailedTest)
----------------------------------------------------------------------
ImportError: Failed to import test module: tests
Traceback (most recent call last):
  File "/usr/lib/python3.10/unittest/loader.py", line 154, in loadTestsFromName
    module = __import__(module_name)
ModuleNotFoundError: No module named 'tests'"""

Traceback (most recent call last):
ModuleNotFoundError: No module named 'tests'"""