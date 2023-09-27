#!/usr/bin/python3
# 8-class_to_json.py
# Matthew Ernst 6628@holbertonstudents.com
"""comment"""

def class_to_json(obj):
    """Serialize class attributes to dictionary
    obj (object): object to be serialized"""
    return (obj.__dict__)
