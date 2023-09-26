#!/usr/bin/python3
# 7-save_to_json_file.py
# Matthew Ernst 6628@holbertonstudents.com
"""Adds arguments to existing list and saves to json file"""
import sys
import json


save_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file
try:
    new_list = load_json("add_item.json")
except FileNotFoundError:
    new_list = []
    new_list.extend(sys.argv[1:])
    save_json(new_list, "add_item.json")
