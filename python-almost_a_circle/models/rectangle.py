#!/usr/bin/python3
# base.py
# Matthew Ernst 6628@holbertonstudents.com
"""Makes a Base Class"""
from models.base import Base


class Rectangle(Base):
    """New Class Base"""
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes Base Class with new attributes"""
        self.width = width
        self.width = height
        self.x = x
        self.y = y
        self.id = id
        
        super().__init__(id)
        