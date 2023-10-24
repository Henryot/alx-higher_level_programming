#!/usr/bin/python3

"""Defines a class Square"""


class Square:
    """
    Class that defines properties of a square by: (based on 1-square.py).

    Attributes:
        size: size of a square (1 side).
    """
    
    def __init__(self, size=0):
        """Creates new instances of square.

        Args:
            size: size of the square (1 side).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
