#!/usr/bin/python3
""" Defines subclass Rectangle """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle inherits from BaseGeometry"""
    def __init__(self, width, height):
        """ Initializes attributes """
        super().integer_validator("width", width)  # either super() or self
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
