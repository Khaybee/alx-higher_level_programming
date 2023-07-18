#!/usr/bin/python3
"""Defines a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new square.

        Args:
            size (int) : The size of the new square.
            x (int) : The x coordinatees of the new square
            y (int) : The y coordinates of the new square
            id (int) : The identit of the new square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
