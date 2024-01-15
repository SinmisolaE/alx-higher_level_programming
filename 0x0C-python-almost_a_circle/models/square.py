#!/usr/bin/python3
""" Define a class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Printable representation of square """
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))

    @property
    def size(self):
        """ Getter method """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter of value"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes """
        if args and len(args) != 0:
            count = 0
            for arg in args:
                if count == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif count == 1:
                    self.size = arg
                elif count == 2:
                    self.x = arg
                elif count == 3:
                    self.y = arg
                count += 1

        elif kwargs and len(kwargs) != 0:
            for k, f in kwargs.items():
                if k == "id":
                    if k is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = f
                elif k == "size":
                    self.size = f
                elif k == "x":
                    self.x = f
                elif k == "y":
                    self.y = f

    def to_dictionary(self):
        """ Returns dictionary representation of attr of square"""
        return {
                'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y
                }
