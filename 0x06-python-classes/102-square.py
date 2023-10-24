#!/usr/bin/python3
"""Defines a class Square with a size and comparison capabilities."""


class Square:
    """Represents a square with a specific size."""

    def __init__(self, size=0):
        """Initializes the square."""
        self.size = size

    @property
    def size(self):
        """Returns the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def __lt__(self, other):
        """Less than comparator."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal to comparator."""
        return self.area() <= other.area()

    def __eq__(self, other):
        """Equality comparator."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Not equal comparator."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparator."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal to comparator."""
        return self.area() >= other.area()
