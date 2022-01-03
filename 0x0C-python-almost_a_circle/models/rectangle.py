#!/usr/bin/python3
"""
Module Contains Rectangle Class
"""


from models.base import Base


class Rectangle(Base):
    """
    Defines rectangle class
    inherits from class Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialises """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

     @property
    def width(self):
        """getter width"""
        return self.__width

    @property
    def height(self):
        """getter height"""
        return self.__height

    @property
    def x(self):
        """getter x"""
        return self.__x

    @property
    def y(self):
        """getter y"""
        return self.__y
