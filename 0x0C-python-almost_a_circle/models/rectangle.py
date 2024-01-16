#!/usr/bin/python3
"""Defines class Rectangle """

from models.base import Base


class Rectangle(Base):
    """ Rectangle inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getter method for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter of width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter method for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter method for height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter method for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter method for x """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter method for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """ setter method for y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns area of rectangle """
        return (self.__width * self.__height)

    def display(self):
        """ Prints the rectangle instance with '#'"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        for x in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            print('#' * self.__width)

    def __str__(self):
        """ Printable representation of rectangle """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Assigns argument to each attribute """
        if args and len(args) != 0:
            count = 0
            for arg in args:
                if count == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif count == 1:
                    self.__width = arg
                elif count == 2:
                    self.__height = arg
                elif count == 3:
                    self.__x = arg
                elif count == 4:
                    self.__y = arg
                count += 1

        elif kwargs and len(kwargs) != 0:
            for k, f in kwargs.items():
                if k == "id":
                    if id is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = f
                elif k == "width":
                    self.width = f
                elif k == "height":
                    self.height = f
                elif k == "x":
                    self.x = f
                elif k == "y":
                    self.y = f

    def to_dictionary(self):
        """ Returns dictionary representation of rectangle """
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
