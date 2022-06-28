#!/usr/bin/python3
"""A locked class called LockedClass"""


class LockedClass:
    """A locked class that only lets the user dynamically create the instance
    attribute 'first_name'
    """
    __slots__ = ["first_name"]
