#!/usr/bin/python3
# 1-my_list.py
# Matthew Ernst 6628@holbertonstudents.com
""" Returns the JSON of the file """
import json


def from_json_string(my_str):
    """ returns an object (Python data structure)
    represented by a JSON string"""
    return (json.loads(my_str))
