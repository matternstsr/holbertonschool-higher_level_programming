#!/usr/bin/python3
# 7-save_to_json_file.py
# Matthew Ernst 6628@holbertonstudents.com


def class_to_json(obj):
    """Serialize class attributes to dictionary
    obj (object): object to be serialized"""
    return (obj.__dict__)
