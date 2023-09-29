#!/usr/bin/python3
# rectangle.py
# Matthew Ernst 6628@holbertonstudents.com
"""Makes a Base Class"""
from models.rectangle import Base


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
            return (f"[Square] ({self.id}) {self.x}/{self.y} - "
                    f"{size}")