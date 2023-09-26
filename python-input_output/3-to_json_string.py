#!/usr/bin/python3
# 3-to_json_string.py
# Matthew Ernst 6628@holbertonstudents.com
""" Returns the JSON of the file """
import json


def to_json_string(my_obj):
    """Returns the rep of the object"""
    return (json.dumps(my_obj))
