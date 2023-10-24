#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Class that defines properties of a square.

    Attributes:
        size: size of a square (1 side).
    """

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.__size = size

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The current square area.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Get or set the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
