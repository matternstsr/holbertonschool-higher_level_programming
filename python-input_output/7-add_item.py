#!/usr/bin/python3
# 7-save_to_json_file.py
# Matthew Ernst 6628@holbertonstudents.com
"""Write a script that adds all arguments to a Python list, and then save them
to a file:
You must use your function save_to_json_file from 5-save_to_json_file.py
You must use your function load_from_json_file from 6-load_from_json_file.py
The list must be saved as a JSON representation in a file named add_item.json
If the file doesn’t exist, it should be created
You don’t need to manage file permissions / exceptions."""

import json


def load_from_json_file(filename):
    """ creates an Object from a JSON file"""
    with open(filename) as doittoit:
        return json.load(doittoit)
