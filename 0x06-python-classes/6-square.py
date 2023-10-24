#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Class that defines properties of a square.

    Attributes:
        __size (int): Size of the square.
        __position (tuple of 2 ints): Position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance.

        Args:
            size (int, optional): Size of the square. Defaults to 0.
            position (tuple of 2 ints, optional): Position of the square.
        """
        self.size = size
        self.position = position

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): Size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get or set the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple of 2 ints): Position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple) or len(value) != 2 or
            not isinstance(value[0], int) or
            not isinstance(value[1], int) or value[0] < 0 or value[1] < 0
        ):
            msg = "position must be a tuple of 2 positive integers"
            raise TypeError(msg)
        self.__position = value

    def my_print(self):
        """Prints the square with the character # considering its position."""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
