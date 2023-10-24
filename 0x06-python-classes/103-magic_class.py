#!/usr/bin/python3
"""Defines a class MagicClass"""
import math


class MagicClass:
    """Class that defines properties of MagicClass."""

    def __init__(self, radius=0):
        """Initializes the MagicClass instance."""
        self.__radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates area of a circle with the given radius."""
        return math.pi * self.__radius ** 2

    def circumference(self):
        """Calculates circumference of a circle with the given radius."""
        return 2 * math.pi * self.__radius
