#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square

    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """initializes the square

        Args:
            size (int): size of a side of the square

        Returns:
            None
        """
        self.size = size

    def area(self):
        """calculates the square's area

        Returns:
            The area of the square
        """
        return int(self.__size) * int(self.__size)

    @property
    def size(self):
        """retrieves the size

        Returns:
            the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size

        Args:
            value (int): side of the square

        Returns:
            the size as value
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints out square of a character

        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(['#' for j in range(self.__size)]))
