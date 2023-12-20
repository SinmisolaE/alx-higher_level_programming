#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Representing a Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialzing size and position"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter method for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size"""
        self.__size = value
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        return self.__size

    def area(self):
        """Return square area"""
        return (self.__size ** 2)

    @property
    def position(self):
        """Getter method for position"""
        return self.position

    @position.setter
    def position(self, value):
        """Passing tuple into the position but also considering exceptoons"""
        if (not isinstance(value, tuple) or
                not all(isinstance(n, int) for n in value) or
                not all(x >= 0 for x in value) or (len(value) != 2)):
            raise TypeError("position must be a tuple of \
                    2 positive integers")
        self.__position = value
        return self.__position

    def my_print(self):
        """Prints the output"""
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]

        for c in range(self.__size):
            [print(" ", end="") for b in range(self.__position[0])]
            [print("#", end="")for j in range(self.__size)]
            print()
