#!/usr/bin/python3
"""contains class square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initiates the class"""
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for side of square"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for side of square"""
        self.width = value
        self.height = value

    def __str__(self):
        """string representation of the square, informal"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id,
                self.x, self.y, self.width)
