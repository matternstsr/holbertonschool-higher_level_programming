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
"""remember! argv[] is the name!!!!! """
"""items.extend(sys.argv[1:]): This code extends the items list with all the
command-line arguments passed to the script, starting from the first argument
(index 1) to the end of the list. It treats sys.argv[1:] as an iterable and
adds all elements from that iterable to the items list. This is what you
typically want when you want to add all command-line arguments.
items.extend(sys.argv[1]): This code attempts to extend the items list with a
single element, which is the first command-line argument (at index 1) as a
whole. This will not work as intended because sys.argv[1] is a single string,
not an iterable of strings. It would result in a TypeError because you cannot
directly extend a list with a single string"""

import sys
import json


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        new_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        new_list = []
    new_list.extend(sys.argv[1:])
    save_to_json_file(new_list, "add_item.json")