#!/usr/bin/python3
# 1-my_list.py
# Matthew Ernst 6628@holbertonstudents.com
""" Returns the JSON of the file """
import json


def from_json_string(my_str):
    """ returns an object (Python data structure)
    represented by a JSON string"""
    """the loads() method for parsing JSON strings.
    Then, you can assign the parsed data to a variable if
    you need too (sure its coming)"""
    return (json.loads(my_str))
