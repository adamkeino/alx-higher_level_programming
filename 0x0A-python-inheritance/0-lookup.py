#!/usr/bin/python3
"""
Lookup function prints out a list of class methods and attributes
"""


def lookup(obj):
    """looks up the obj object attributes and methods"""
    object_methods = [method_name for method_name in dir(obj)
            if callable(getattr(obj, method_name))]

    return object_methods
