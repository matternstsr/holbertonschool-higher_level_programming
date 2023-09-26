#!/usr/bin/python3
# 1-my_list.py
# Matthew Ernst 6628@holbertonstudents.com
"""Write a function that writes an Object to a text file, using a JSON
representation:
Prototype: def save_to_json_file(my_obj, filename):
You must use the with statement
You don’t need to manage exceptions if the object can’t be serialized.
You don’t need to manage file permission exceptions.
combining the read and write json"""

import json


def save_to_json_file(my_obj, filename):
    """ Saves sjon to specified filename"""
        """write a string to the file"""
    with open(filename, mode="w", encoding="utf-8") as doittoit:
        return json.dumps(my_obj)

