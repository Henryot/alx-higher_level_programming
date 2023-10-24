#!/usr/bin/python3
"""Defines a class Square with a size and position"""


class Square:
    """Represents a square with a specific size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #."""
        if self.__size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for i in range(self.__size):
            print(' ' * self.position[0] + '#' * self.__size)

    def __str__(self):
        """Returns a string representation of the square."""
        if self.__size == 0:
            return ""
        squares = [
            ' ' * self.position[0] + '#' * self.__size
            for _ in range(self.__size)
        ]
        return "\n" * self.position[1] + "\n".join(squares)
