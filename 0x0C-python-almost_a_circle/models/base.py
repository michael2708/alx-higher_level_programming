#!/usr/bin/python3
"""
Model Contains Base Class
"""


class Base():
    """
    defines class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize id, increment class attribute if no id and set as id"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
