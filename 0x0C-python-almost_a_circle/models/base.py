#!/usr/bin/python3
"""
contains base class
"""


class Base:
    """the class itself"""
    __nb_objects = 0
    def __init__(self, id=None):
        """constructor for the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
